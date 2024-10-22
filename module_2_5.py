def get_matrix(n, m, value): #Объявил функцию get_matrix и напиcал в ней параметры n, m и значение
    matrix = [] # Создал пустой список matrix внутри функции get_matrix.
    for a in range(0, n):#первый (внешний) цикл for для количества строк матрицы, n повторений.
        matrix2 = []
        for b in range(0, m):#второй (внутренний) цикл for для количества столбцов матрицы, m повторений.
            matrix2.append(value)
        matrix.append(matrix2)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1) #вывод на экран (консоль) результат работы функции get_matrix.
print(result2)
print(result3)


