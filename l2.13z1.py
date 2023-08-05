class Division(Exception):
    def __init__(self):
        super().__init__("Деление на ноль недопустимо")

try:
    n = int(input("Введите числитель: "))
    d = int(input("Введите знаменатель: "))

    if d == 0:
        raise Division()

    result = n / d
    print("Результат деления:", result)

except Division as e:
    print("Ошибка:", e)
except ValueError:
    print("Ошибка: Введите корректное число")
