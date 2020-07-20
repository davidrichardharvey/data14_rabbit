from time import sleep
from random import randint

class Rabbit:

    def __init__(self):
        self.months = 0

    def advance_time(self, months=None):
        sleep(1)
        if not months:
            months = self.months
        months += 1
        self.months = months
        return months

    def number_of_babies(self, pregnant_rabbits):
        sum = 0
        for i in range(pregnant_rabbits):
            num_babies = randint(1, 14)
            sum += num_babies
        return sum