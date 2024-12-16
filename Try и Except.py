def add_everything_up(a, b):
    # Проверяем, разные ли типы a и b
    if type(a) != type(b):
        # Если типы разные, возвращаем их строковое представление
        return str(a) + str(b)

    # Если оба аргумента числа (int или float), складываем их
    if isinstance(a, (int, float)):
        return a + b

    # Если оба аргумента строки, объединяем их
    if isinstance(a, str):
        return a + b


# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456
