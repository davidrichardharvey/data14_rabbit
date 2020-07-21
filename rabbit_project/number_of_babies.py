from rabbit_project.rabbit import Rabbit
from random import randint

class RabbitBirths(Rabbit):

    def __init__(self):
        super().__init__()
        self.birth = 0
        self.pregnancies = 0
        self.fertile_males = self.fertile_rabbits()[0]
        self.fertile_females = self.fertile_rabbits()[0]

    def fertile_rabbits(self, male_ages=None, female_ages=None):
        if male_ages is None:
            male_ages = self.male_age
        if female_ages is None:
            female_ages = self.female_age
        fertile_males = 0
        fertile_females = 0
        for key in male_ages:
            if key >= 3:
                fertile_males += male_ages[key]
        for key in female_ages:
            if key >= 3:
                fertile_females += female_ages[key]
        return [fertile_males, fertile_females]

    def new_pregnancies(self, fertile_male=None, fertile_female=None):
        if fertile_male is None:
            fertile_male = self.fertile_males
        if fertile_female is None:
            fertile_female = self.fertile_females
        new_pregnancies = min(fertile_male, fertile_female)
        self.pregnancies = new_pregnancies
        return new_pregnancies

    def number_of_babies(self, new_pregnancies=None):
        if new_pregnancies is None:
            new_pregnancies = self.pregnancies
        num_of_births = 0
        for i in range(new_pregnancies):
            num_babies = randint(1, 14)
            num_of_births += num_babies
        self.birth = num_of_births
        return num_of_births


testing = RabbitBirths()

print(testing.fertile_rabbits({3: 1}, {3: 1}))
print(testing.new_pregnancies())
print(testing.number_of_babies())