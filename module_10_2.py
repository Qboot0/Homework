import threading
import time
from threading import Thread


class Kinght (threading.Thread):
   def __init__(self, name, power):
       super().__init__()
       self.name = name
       self.power = power
       self.enemies = 100

   def run(self):
       print(f"{self.name}, на нас напали!")
       days = 0

       while self.enemies > 0:
           time.sleep(1)
           days += 1
           self.enemies -= self.power
           remaining_enemies = max(self.enemies, 0)
           print(f"{self.name}, сражается {days} день(дня)..., осталось {remaining_enemies} воинов.")

       print(f"{self.name} одержал победу спустя {days} дней(дня)!")
first_kinght = Kinght('Sir Lancelot', 10)
second_kinght = Kinght('Sir Galahad', 20)
first_kinght.start()
second_kinght.start()
first_kinght.join()
second_kinght.join()

print("Все битвы закончились!")