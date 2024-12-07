import random
class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed
    def move(self, dx, dy, dz):
        if self._cords[2] + dz < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)
class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True
    def lay_eggs(self):
        number_of_eggs = random.randint(1, 4)
        print(f"Here are(is) {number_of_eggs} eggs for you")
class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dz = abs(dz)
        if self._cords[2] - dz < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[2] -= dz
        self.speed /= 2
class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
        self.sound = "Click-click-click"
Db = Duckbill(24)
print(Db.live)
print(Db.beak)
Db.speak()
Db.attack()
Db.move(5, 3, 8)
Db.get_cords()
Db.dive_in(1)
Db.get_cords()
Db.lay_eggs()

