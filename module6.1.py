class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Fruit(Plant):
    def __init__ (self, name):
        super().__init__(name)
        self.edible = True
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
a1 = Predator("медветь")
a2 = Mammal("гризли")
p1 = Flower("роза")
p2 = Fruit("мандарин")
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)