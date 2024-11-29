import json
from datetime import datetime
import os
import csv


class TasksManager:
    FILE_NAME = "tasks.json"

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_tasks(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def menu(self):
        while True:
            print("\nУправление задачами")
            print("1. Добавить задачу")
            print("2. Просмотреть задачи")
            print("3. Отметить задачу как выполненную")
            print("4. Редактировать задачу")
            print("5. Удалить задачу")
            print("6. Импорт файла")
            print("7. Экспорт файла")
            print("8. Назад в главное меню")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_task_done()
            elif choice == "4":
                self.edit_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                self.import_csv()
            elif choice == '7':
                self.export_csv()
            elif choice == '8':
                break
            else:
                print("Неверный ввод. Попробуйте снова.")

    def add_task(self):
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        due_date = input("Введите срок выполнения (ДД-ММ-ГГГГ): ")
        priority = input("Введите приоритет (Высокий, Средний, Низкий): ")
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "done": False,
            "priority": priority,
            "due_date": due_date
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Задача добавлена.")

    def view_tasks(self):
        if not self.tasks:
            print("Нет задач.")
            return
        for task in self.tasks:
            status = "✔" if task["done"] else "✘"
            print(f"[{task['id']}] {task['title']} - {task['priority']} - {task['due_date']} [{status}]")

    def mark_task_done(self):
        task_id = int(input("Введите ID выполненной задачи: "))
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            print("Задача не найдена.")
            return
        task["done"] = True
        self.save_tasks()
        print("Задача отмечена как выполненная.")

    def edit_task(self):
        task_id = int(input("Введите ID задачи для редактирования: "))
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if not task:
            print("Задача не найдена.")
            return
        task["title"] = input(f"Новое название (текущее: {task['title']}): ") or task["title"]
        task["description"] = input(f"Новое описание (текущее: {task['description']}): ") or task["description"]
        task["due_date"] = input(f"Новый срок (текущий: {task['due_date']}): ") or task["due_date"]
        task["priority"] = input(f"Новый приоритет (текущий: {task['priority']}): ") or task["priority"]
        self.save_tasks()
        print("Задача обновлена.")

    def delete_task(self):
        task_id = int(input("Введите ID задачи для удаления: "))
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self.save_tasks()
        print("Задача удалена.")

    def import_csv(self):
        file_name = input("Введите имя CSV-файла для импорта: ")
        try:

            with open(file_name, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for item in reader:
                    item['id'] = int(item['id'])
                    item['done'] = bool(item['done'])
                    self.tasks.append(item)
            self.save_tasks()
        except FileNotFoundError:
            print(f'Файл не найден.')

    def export_csv(self):
        try:
            with open('tasks_export.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'title', 'description', 'done', 'priority', 'due_date'])
                writer.writeheader()
                writer.writerows(self.tasks)
        except Exception as e:
            print(e)
