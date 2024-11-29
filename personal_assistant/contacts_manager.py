import json
import csv
import os


class ContactsManager:
    FILE_NAME = "contacts.json"

    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_contacts(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(self.contacts, file, ensure_ascii=False, indent=4)

    def menu(self):
        while True:
            print("\nУправление контактами")
            print("1. Добавить контакт")
            print("2. Поиск контакта")
            print("3. Редактировать контакт")
            print("4. Удалить контакт")
            print("5. Импорт файла")
            print("6. Экспорт файла")
            print("7. Назад в главное меню")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.search_contact()
            elif choice == "3":
                self.edit_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == '5':
                self.import_csv()
            elif choice == '6':
                self.export_csv()
            elif choice == "7":
                break
            else:
                print("Неверный ввод. Попробуйте снова.")

    def add_contact(self):
        name = input("Введите имя контакта: ")
        phone = input("Введите номер телефона: ")
        email = input("Введите адрес электронной почты: ")
        contact = {
            "id": len(self.contacts) + 1,
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print("Контакт добавлен.")

    def search_contact(self):
        query = input("Введите имя или номер телефона для поиска: ")
        results = [c for c in self.contacts if query in c["name"] or query in c["phone"]]
        if not results:
            print("Контакты не найдены.")
            return
        for contact in results:
            print(f"[{contact['id']}] {contact['name']} - {contact['phone']} - {contact['email']}")

    def edit_contact(self):
        contact_id = int(input("Введите ID контакта для редактирования: "))
        contact = next((c for c in self.contacts if c["id"] == contact_id), None)
        if not contact:
            print("Контакт не найден.")
            return
        contact["name"] = input(f"Новое имя (текущее: {contact['name']}): ") or contact["name"]
        contact["phone"] = input(f"Новый телефон (текущий: {contact['phone']}): ") or contact["phone"]
        contact["email"] = input(f"Новая почта (текущая: {contact['email']}): ") or contact["email"]
        self.save_contacts()
        print("Контакт обновлен.")

    def delete_contact(self):
        contact_id = int(input("Введите ID контакта для удаления: "))
        self.contacts = [c for c in self.contacts if c["id"] != contact_id]
        self.save_contacts()
        print("Контакт удален.")

    def import_csv(self):
        file_name = input("Введите имя CSV-файла для импорта: ")
        try:

            with open(file_name, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for item in reader:
                    item['id'] = int(item['id'])
                    self.contacts.append(item)
            self.save_contacts()
        except FileNotFoundError:
            print(f'Файл не найден.')

    def export_csv(self):
        try:
            with open('contacts_export.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'name', 'phone', 'email'])
                writer.writeheader()
                writer.writerows(self.contacts)
        except Exception as e:
            print(e)
