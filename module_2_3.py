my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0 # обращение к индексу

while index < len(my_list):#сравнивание текущего индекса и длины списка к (функции len()).

    if my_list[index] < 0:
        break# прерывает цыкл

    if my_list[index] > 0:
        print(my_list[index])

    index += 1