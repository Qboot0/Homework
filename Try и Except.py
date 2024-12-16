def add_everything_up(a, b):
    if type(a) != type(b):
        return str(a) + str(b)

    if isinstance(a, (int, float)):
        return a + b

    if isinstance(a, str):
        return a + b


print(add_everything_up(123.456, 'строка'))  
print(add_everything_up('яблоко', 4215))  
print(add_everything_up(123.456, 7))  
