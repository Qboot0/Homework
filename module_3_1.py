
calls=0#Создать переменную calls = 0 вне функций.
def count_calls ():# Создаём функцию count_calls и изменять в ней значение переменной calls.
    global calls
    calls+=1
def string_info(string):# Создаём функцию string_info с параметром string
    count_calls()
    return(len(string),string.upper(), string.lower())
def is_contains(string, list_to_searh):# Создаём функцию is_contains с двумя параметрами string и list_to_search
    count_calls()
    return string.upper() in [s.upper() for s in list_to_searh]
print(string_info('WOLF'))
print(string_info('tiger'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) 
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)#Вывести значение переменной calls на экран(в консоль).
