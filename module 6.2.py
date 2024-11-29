class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Green', 'Blue', 'White', 'Black',]
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str (__model)#модель
        self.__engine_power = int(__engine_power)#мощность
        self.__color = str(__color)#цвет
    def get_model(self):
        print(f"Модель: {self.__model}")
    def get_horsepower(self):
        print(f"Мощность двигателя:{self.__engine_power}")
    def get_color(self):
        print(f"Цвет:{self.__color}")
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS]
        if new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 4

avto1 = Sedan('Dima', 'Supra',387, 'red')
avto1.print_info()
avto1.set_color('Мальновый')
avto1.set_color('Black')
avto1.owner = 'Max'
avto1.print_info()