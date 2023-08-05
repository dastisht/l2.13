class NegativeRectangle(Exception):
    def __init__(self):
        super().__init__("Отрицательные размеры прямоугольника недопустимы")

try:
    l = float(input("Введите длину прямоугольника: "))
    w = float(input("Введите ширину прямоугольника: "))

    if l < 0 or w < 0:
        raise NegativeRectangle()

    area = l * w
    print("Площадь прямоугольника:", area)

except NegativeRectangle as e:
    print("Ошибка:", e)
except ValueError:
    print("Ошибка: Введите корректные размеры")
