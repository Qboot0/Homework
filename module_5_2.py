
class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        title = str(f"Название:{self.name},количество этажей:{self.number_of_floors}")
        return title

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Фкация', 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
