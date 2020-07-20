from time import sleep
from random import randint

class Rabbit:
    def __init__(self):
        self.number_males = 1
        self.number_females = 1
        self.total = self.number_males + self.number_females
        self.months = 0
        self.female_age = {3: 1}  # {age: count_with_age}
        self.male_age = {3: 1}

    def _set_initial(self, month=None, num_males=None, num_females=None, male_age=None, female_age=None):
        if not num_males:
            num_males = self.number_males
        if not num_females:
            num_females = self.number_females
        if not month:
            month = self.months
        if not male_age:
            male_age = self.male_age
        if not female_age:
            female_age = self.female_age
        total = num_males + num_females
        self.total = total
        return [total, month, male_age[3], female_age[3]]

    def advance_time(self, months_since_start=None):
        sleep(1)
        if months_since_start is None:
            months_since_start = self.months
        months_since_start += 1
        self.months = months_since_start
        return months_since_start

    def number_of_babies(self, pregnant_rabbits):
        sum = 0
        for i in range(pregnant_rabbits):
            num_babies = randint(1, 14)
            sum += num_babies
        return sum
