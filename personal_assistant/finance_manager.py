import json
import csv
import os


class FinanceManager:
    FILE_NAME = "finance.json"

    def __init__(self):
        self.records = self.load_records()

    def load_records(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_records(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(self.records, file, ensure_ascii=False, indent=4)

    def menu(self):
        while True:
            print("\nУправление финансовыми записями")
            print("1. Добавить запись")
            print("2. Просмотреть записи")
            print("3. Фильтровать записи")
            print("4. Генерация отчётов")
            print('5. Импорт файла')
            print('6. Экспорт файла')
            print("7. Назад в главное меню")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_record()
            elif choice == "2":
                self.view_records()
            elif choice == "3":
                self.filter_records()
            elif choice == "4":
                self.generate_report()
            elif choice == '5':
                self.import_csv()
            elif choice == '6':
                self.export_csv()
            elif choice == "7":
                break
            else:
                print("Неверный ввод. Попробуйте снова.")

    def add_record(self):
        try:
            amount = float(input("Введите сумму операции (положительная — доход, отрицательная — расход): "))
            category = input("Введите категорию (например, 'Еда', 'Транспорт'): ")
            date = input("Введите дату (ДД-ММ-ГГГГ): ")
            description = input("Введите описание операции: ")
            record = {
                "id": len(self.records) + 1,
                "amount": amount,
                "category": category,
                "date": date,
                "description": description
            }
            self.records.append(record)
            self.save_records()
            print("Запись добавлена.")
        except ValueError:
            print("Ошибка ввода. Сумма должна быть числом.")

    def view_records(self):
        if not self.records:
            print("Нет записей.")
            return
        for record in self.records:
            print(
                f"[{record['id']}] {record['date']} - {record['category']} - {record['amount']} - {record['description']}")

    def filter_records(self):
        category = input("Введите категорию для фильтрации: ")
        filtered = [r for r in self.records if r["category"].lower() == category.lower()]
        if not filtered:
            print("Записей не найдено.")
            return
        for record in filtered:
            print(f"[{record['id']}] {record['date']} - {record['amount']} - {record['description']}")

    def generate_report(self):
        print("\nОтчёт о финансовой активности")
        income = sum(r["amount"] for r in self.records if r["amount"] > 0)
        expenses = sum(r["amount"] for r in self.records if r["amount"] < 0)
        balance = income + expenses
        print(f"Общий доход: {income}")
        print(f"Общие расходы: {expenses}")
        print(f"Баланс: {balance}")

    def import_csv(self):
        file_name = input("Введите имя CSV-файла для импорта: ")
        try:

            with open(file_name, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for item in reader:
                    item['id'] = int(item['id'])
                    item['amount'] = float(item['amount'])
                    self.records.append(item)
            self.save_records()
        except FileNotFoundError:
            print(f'Файл не найден.')

    def export_csv(self):
        try:
            with open('records_export.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'amount', 'category', 'date', 'description'])
                writer.writeheader()
                writer.writerows(self.records)
        except Exception as e:
            print(e)
