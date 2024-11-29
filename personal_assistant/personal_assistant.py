import os
from notes_manager import NotesManager
from tasks_manager import TasksManager
from contacts_manager import ContactsManager
from finance_manager import FinanceManager
from calculator import Calculator


def main():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")
        if choice == "1":
            notes_manager = NotesManager()
            notes_manager.menu()
        elif choice == '2':
            task_manager = TasksManager()
            task_manager.menu()
        elif choice == '3':
            contact_manager = ContactsManager()
            contact_manager.menu()
        elif choice == '4':
            finance_manager = FinanceManager()
            finance_manager.menu()
        elif choice == '5':
            calculator = Calculator()
            calculator.run()
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == '__main__':
    main()
