class NegativeIndexError(Exception):
    def __init__(self):
        super().__init__("Отрицательные индексы недопустимы")

try:
    l = [1, 2, 3, 4, 5]
    i = int(input("Введите индекс элемента: "))

    if i < 0:
        raise IndexError()

    element = l[i]
    print("Выбранный элемент:", element)

except NegativeIndexError as e:
    print("Ошибка:", e)
except IndexError:
    print("Ошибка: Индекс выходит за пределы списка")
except ValueError:
    print("Ошибка: Введите корректный индекс")
