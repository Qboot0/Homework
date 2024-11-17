class House:#Создайте класс House
    def __init__(self, name, number_of_floors):#Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
       self.name = name#нутри метода __init__ создайте атрибуты объекта self.name
       self.number_of_floors = number_of_floors#и self.number_of_floors, присвойте им переданные значения.

    def go_to(self, new_floor):#Создайте метод go_to с параметром new_floor
        floor = 0
        print(f'Здание {self.name} имеет {self.number_of_floors} этажей \nПоднимаемся на {new_floor}-й')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'{new_floor} - такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)


hightower = House('ЖК Горский', 18)
warehouse = House('Домик в деревне', 2)

hightower.go_to(5)
warehouse.go_to(10)