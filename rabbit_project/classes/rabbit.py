from random import randint
import numpy as np


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
        if len(self.list) < 49:
            for i in range(0, len(self.list)):
                total_pop += (self.list[i]['Males'] + self.list[i]['Females'])
            self.total_population = total_pop
        else:
            for i in range(0, len(self.list[:48])):
                total_pop += (self.list[i]['Males'] + self.list[i]['Females'])
            self.total_population = total_pop + self.vulnerable_females + self.vulnerable_males
        return self.total_population

    def init_list(self):
        # This sets the initial list of 60 items with all ages of rabbits, assuming they die at 5 years old
        new_list = []
        new_list.append({"Males": 0, "Females": 0})
        new_list.append({"Males": 0, "Females": 0})
        new_list.append({"Males": 0, "Females": 0})
        new_list.append({"Males": 1, "Females": 1})
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
        current_preg = self.pregnancies.pop(0)
        sigma = (current_preg - 1)/(sqrt(12))
        mu = 7.5 * current_preg
        new_children = round(np.random.normal(mu, sigma, 1))
        self.new_babies += new_children

    def calc_gender_totals(self):
        # This calculates the total number of males and females in the rabbit list
        self.males = 0
        self.females = 0
        if len(self.list) < 49:
            for generation in self.list:
                self.males += generation['Males']
                self.females += generation['Females']
        else:
            for generation in self.list:
                self.males[:48] += generation['Males'] + self.vulnerable_males
                self.females[:48] += generation['Females'] + self.vulnerable_females


    def pregnant_rabbits(self):
        if len(self.list) < 49:
            # This calculates the number of rabbits that can be pregnant and returns a number of rabbits who become pregnant
            fertile_males = self.males - self.list[0]['Males'] - self.list[1]['Males'] - self.list[2]['Males']
            fertile_females = self.females - self.list[0]['Females'] - self.list[1]['Females'] - self.list[2]['Females'] - \
                            self.pregnancies[1]
            pregnancies = min(fertile_females, 10 * fertile_males)
            self.pregnancies.append(pregnancies)
            return self.pregnancies

        def old_pregnant_rabbits(self):
            if len(self.list) >= 49:
                # This calculates the number of rabbits that can be pregnant and returns a number of rabbits who become pregnant
                fertile_males = self.males[:48] - self.list[0]['Males'] - self.list[1]['Males'] - self.list[2]['Males']
                fertile_females = self.females[:48] - self.list[0]['Females'] - self.list[1]['Females'] - self.list[2]['Females'] - \
                            self.pregnancies[1]
                pregnancies = min(fertile_females, 10 * fertile_males)
                self.pregnancies.append(pregnancies)
                old_pregnancies = min(vulnerable_females, 10 * vulnerable_males)
                self.pregnancies += old_pregnancies
                return self.pregnancies


    def rabbit_deaths_new(self):
        if len(self.list) > 48:
            for key in self.list[48:]:
                self.vulnerable_females += key['Females']
                self.vulnerable_males += key['Males']
            deaths = 0
            if self.vulnerable_males < 500:
                for each in range(0, self.vulnerable_males):
                    death_roll = randint(1, 11)
                    if death_roll == 1:
                        deaths += 1
                        self.vulnerable_males -= 1
            else:
                n, p = self.vulnerable_males, 0.1
                deaths = np.random.binomial(n, p, 1)[0]
                self.vulnerable_males -= deaths
                self.deaths_total += deaths
            deaths = 0
            if self.vulnerable_males < 500:
                for each in range(0, self.vulnerable_males):
                    death_roll = randint(1, 11)
                    if death_roll == 1:
                        deaths += 1
                        self.vulnerable_males -= 1
            else:
                n, p = self.vulnerable_males, 0.1
                    deaths = np.random.binomial(n, p, 1)[0]
                    self.vulnerable_males -= deaths
                    self.deaths_total += deaths
        

        