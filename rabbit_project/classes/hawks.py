from random import randint
import rabbit_project.config_file as config
from numpy import random

class Hawk:
    def __init__(self):
        self.total_population = 0
        self.males = int(config.h_starting_males())
        self.females = int(config.h_starting_females())
        self.list = self.init_list()
        self.min = int(config.h_babies_min())
        self.max = int(config.h_babies_max())
        self.pregnancies = [0, 1]  # First index is the birthing females, second index is pregnant females
        self.new_babies = 0
        self.deaths_total = 0
    def calculate_total_pop(self):
        # This method goes through the list of hawks and counts up all males and females
        total_pop = 0
        for i in range(0, len(self.list)):
            total_pop += (self.list[i]['Males'] + self.list[i]['Females'])
        self.total_population = total_pop
        return total_pop
    def init_list(self):
        # This sets the initial list of 60 items with all ages of hawks, assuming they die at 5 years old
        new_list = []
        for each in range(0, 60):
            new_list.append({"Males": 0, "Females": 0})
        new_list[int(config.h_starting_age())] = {"Males": self.males, "Females": self.females}
        return new_list
    def assign_genders(self):
        # This assigns genders to hawks at birth and appends these values to the list of hawks
        males = 0
        females = 0
        for baby in range(0, self.new_babies):
            gender = ['M', 'F'][randint(0, 1)]
            if gender == 'M':
                males += 1
            elif gender == 'F':
                females += 1
        self.list.append({'Males': males, 'Females': females})
    def birth_children(self):
        # This calculates the number of hawks born based on the number of birthing females
        self.new_babies = 0
        for each in range(0, self.pregnancies.pop(0)):
            new_children = randint(self.min, self.max)
            self.new_babies += new_children
    def calc_gender_totals(self):
        # This calculates the total number of males and females in the hawks list
        self.males = 0
        self.females = 0
        for generation in self.list:
            self.males += generation['Males']
            self.females += generation['Females']
    def hawks_dead(self):
        generation_deaths = self.list.pop(0)
        deaths = generation_deaths['Males'] + generation_deaths['Females']
        self.deaths_total += deaths
    def pregnant_hawks(self):
        # This calculates the number of hawks that can be pregnant and returns a number of hawks who become pregnant
        # Rabbits - 2 Month old Rabbits - 1 Month old Rabbits - (Pregnant Females) - (Females who have given birth)
        fertile_males = self.males - self.list[0]['Males'] - self.list[1]['Males'] - self.list[2]['Males'] - self.list[3]['Males'] \
                        - self.list[4]['Males'] - self.list[5]['Males'] - self.list[6]['Males'] - self.list[7]['Males'] - self.list[8]['Males'] \
                        - self.list[9]['Males'] - self.list[10]['Males']
        fertile_females = self.females - self.list[0]['Females'] - self.list[1]['Females'] - self.list[2]['Females'] - self.list[3]['Females'] \
                        - self.list[4]['Females'] - self.list[5]['Females'] - self.list[6]['Females'] - self.list[7]['Females'] - self.list[8]['Females'] \
                        - self.list[9]['Females'] - self.list[10]['Females'] - self.pregnancies[0]
        potential_pregnancies = min(fertile_females, fertile_males)
        n, p = potential_pregnancies, 0.9
        num_pregnancies = random.binomial(n, p, 1)[0]
        self.pregnancies.append(num_pregnancies)
        return num_pregnancies