def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


def main():
    print("=== BASIC CALCULATOR ===")

    while True:
        print("\nВыберите операцию:")
        print("1 - Сложение")
        print("2 - Вычитание")
        print("3 - Умножение")
        print("4 - Деление")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == "0":
            print("Программа завершена.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Ошибка: выберите операцию от 1 до 4.")
            continue

        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: необходимо ввести число.")
            continue

        if choice == "1":
            result = add(a, b)

        elif choice == "2":
            result = subtract(a, b)

        elif choice == "3":
            result = multiply(a, b)

        else:
            result = divide(a, b)

        print(f"Результат: {result}")


if __name__ == "__main__":
    main()