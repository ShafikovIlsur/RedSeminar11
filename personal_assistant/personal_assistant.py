import os
from notes_manager import NotesManager


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
            NotesManager().menu()
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == '__main__':
    main()
