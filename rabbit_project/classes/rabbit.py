from random import randint
from numpy import random


class Rabbit:
    def __init__(self):
        self.total_population = 0
        self.males = 1
        self.females = 1
        self.list = self.init_list()
        self.pregnancies = [0, 1]  # First index is the birthing females, second index is pregnant females
        self.new_babies = 0
        self.deaths_total = 0
        self.new_generation = []
        self.vulnerable_females = 0
        self.vulnerable_males = 0

    def calculate_total_pop(self):
        # This method goes through the list of rabbits and counts up all males and females
        total_pop = 0
        for i in range(0, len(self.list)):
            total_pop += (self.list[i]['Males'] + self.list[i]['Females'])
        self.total_population = total_pop
        return total_pop

    def init_list(self):
        # This sets the initial list of 60 items with all ages of rabbits, assuming they die at 5 years old
        new_list = []
        new_list.append({"Males": 0, "Females": 0})
        new_list.append({"Males": 0, "Females": 0})
        new_list.append({"Males": 1, "Females": 1})
        for each in range(0, 57):
            new_list.append({"Males": 0, "Females": 0})

        return new_list

    def assign_genders(self):
        # This assigns genders to rabbits at birth and appends these values to the list of rabbits
        males = 0
        females = 0
        for baby in range(0, self.new_babies):
            gender = ['M', 'F'][randint(0, 1)]
            if gender == 'M':
                males += 1
            elif gender == 'F':
                females += 1
        self.new_generation = {'Males': males, 'Females': females}
        self.list = [self.new_generation] + self.list

    def birth_children(self):
        # This calculates the number of rabbits born based on the number of birthing females
        self.new_babies = 0
        for each in range(0, self.pregnancies.pop(0)):
            new_children = randint(1, 14)
            self.new_babies += new_children

    def calc_gender_totals(self):
        # This calculates the total number of males and females in the rabbit list
        self.males = 0
        self.females = 0
        for generation in self.list:
            self.males += generation['Males']
            self.females += generation['Females']

    def rabbits_dead(self):
        generation_deaths = self.list.pop(0)
        deaths = generation_deaths['Males'] + generation_deaths['Females']
        self.deaths_total += deaths

    def pregnant_rabbits(self):
        # This calculates the number of rabbits that can be pregnant and returns a number of rabbits who become pregnant
        # Rabbits - 2 Month old Rabbits - 1 Month old Rabbits - (Pregnant Females) - (Females who have given birth)
        fertile_males = self.males - self.list[0]['Males'] - self.list[1]['Males']
        fertile_females = self.females - self.list[0]['Females'] - self.list[1]['Females'] - self.pregnancies[0]
        potential_pregnancies = min(fertile_females, fertile_males * 10)
        n, p = potential_pregnancies, 0.5
        num_pregnancies = random.binomial(n, p, 1)[0]
        self.pregnancies.append(num_pregnancies)
        return num_pregnancies



