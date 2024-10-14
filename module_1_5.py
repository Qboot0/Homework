immutable_var = (1,2 ,"Hello")
print(immutable_var)
immutable_var = (1,2 , "hello") * 3 #кортеж относится к неизменяемым типам данных, тем не менее внутри он может содержать изменяемые типы.
print(immutable_var)
mutable_list = [1,2, "hello"]
mutable_list [0] = 20
print(mutable_list)