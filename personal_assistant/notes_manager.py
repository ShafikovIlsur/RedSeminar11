from datetime import datetime
import json
import os
import csv


class NotesManager:
    FILE_NAME = 'notes.json'

    def __init__(self):
        self.notes = self.load_notes()

    def menu(self):
        while True:
            print("\nУправление заметками")
            print("1. Создать заметку")
            print("2. Просмотреть все заметки")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Импорт заметок")
            print("6. Экспорт заметок")
            print("7. Назад в главное меню")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.create_note()
            elif choice == "2":
                self.get_notes()
            elif choice == "3":
                self.edit_note()
            elif choice == "4":
                self.delete_note()
            elif choice == "5":
                self.import_csv()
            elif choice == '6':
                self.export_csv()
            elif choice == "7":
                break
            else:
                print("Неверный ввод. Попробуйте снова.")

    def load_notes(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        else:
            with open(self.FILE_NAME, 'r', encoding='utf-8') as f:
                return json.load(f)

    def save_notes(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=4)

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "timestamp": timestamp
        }
        self.notes.append(note)
        self.save_notes()
        print("Заметка создана успешно!")

    def get_notes(self):
        if len(self.notes) == 0:
            print('Заметки отсутствуют.')
            return
        else:
            for note in self.notes:
                print(f'id: {note['id']}\n'
                      f'title: {note['title']}\n'
                      f'content: {note['content']}'
                      f'\ntimestamp: {note['timestamp']}')

    def edit_note(self):
        note_id = int(input("Введите id заметки"))
        note = next((note for note in self.notes if note['id'] == note_id), None)
        if note is None:
            print('Такой заметки нет.')
            return

        new_title = input("Введите новый заголовок ")
        new_content = input('Введите новое описание ')
        new_timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        note['title'] = new_title
        note['content'] = new_content
        note['timestamp'] = new_timestamp
        self.save_notes()
        print('Заметка отредактирована.')

    def delete_note(self):
        note_id = int(input("Введите id заметки для удаления: "))
        if next((note for note in self.notes if note['id'] == note_id), None) is None:
            print('Такой заметки нет.')
            return
        self.notes = [n for n in self.notes if n["id"] != note_id]
        self.save_notes()
        print("Заметка удалена.")

    def import_csv(self):
        file_name = input("Введите имя CSV-файла для импорта: ")
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for item in reader:
                    self.notes.append(item)
            self.save_notes()
        except FileNotFoundError:
            print(f'Файл не найден.')

    def export_csv(self):
        try:
            with open('notes_export.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'title', 'content', 'timestamp'])
                writer.writeheader()
                writer.writerows(self.notes)
        except Exception as e:
            print(e)
