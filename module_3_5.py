def get_multiplird_digits(number):
    number = int(number) # Убераем 0 в начале
    str_number = str(number)
    first = int(str_number[0])
    while str_number.endswith("0"):#Убираем 0 в конце
        str_number = str_number[:len(str_number)-1]
    if len(str_number) > 1:
        return  first * get_multiplird_digits(int(str_number[1:]))
    else:
        return first
num = input('Введите число: ')
print( get_multiplird_digits(num))
