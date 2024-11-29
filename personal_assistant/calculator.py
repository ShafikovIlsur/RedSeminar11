class Calculator:
    def run(self):
        print("\nКалькулятор")
        while True:
            expression = input("Введите выражение для расчёта (или 'exit' для выхода): ")
            if expression.lower() == "exit":
                break
            try:
                result = eval(expression, {"__builtins__": None}, {})
                print(f"Результат: {result}")
            except ZeroDivisionError:
                print("Ошибка: деление на ноль.")
            except Exception as e:
                print(f"Ошибка: некорректное выражение ({e}).")
