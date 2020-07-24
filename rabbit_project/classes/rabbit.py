from random import randint
import numpy as np
import rabbit_project.config_file as config


class Rabbit:
    def __init__(self):
        self.total_population = 0
        self.starting_age = int(config.r_starting_age())
        self.males = int(config.r_starting_males())
        self.females = int(config.r_starting_females())
        self.list = self.init_list()
        self.min = int(config.r_babies_min())
        self.max = int(config.r_babies_max())
        self.pregnancy_chance = float(config.r_pregnancy_chance())
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
            self.total_population = (total_pop)
        else:
            for i in range(0, len(self.list[:48])):
                total_pop += (self.list[i]['Males'] + self.list[i]['Females'])
            self.total_population = total_pop + self.vulnerable_females + self.vulnerable_males
        return self.total_population

    def init_list(self):
        # This sets the initial list of 60 items with all ages of rabbits, assuming they die at 5 years old
        new_list = []
        while len(new_list) <= (int(config.r_starting_age()) + 1):
            new_list.append({"Males": 0, "Females": 0})
        new_list[self.starting_age + 1] = {"Males": self.males, "Females": self.females}
        return new_list

    def assign_genders(self):
        # This assigns genders to rabbits at birth and appends these values to the list of rabbits
        males = 0
        females = 0
        if self.new_babies > 1000:
            n, p = self.new_babies, 0.5
            males = np.random.binomial(n, p, 1)[0]
            females = self.new_babies - males
        else:
            for baby in range(0, self.new_babies):
                gender = ['M', 'F'][randint(0, 1)]
                if gender == 'M':
                    males += 1
                elif gender == 'F':
                    females += 1
        self.list.append({'Males': (males), 'Females': (females)})

    def birth_children(self):
        # This calculates the number of rabbits born based on the number of birthing females
        self.new_babies = 0
        if self.pregnancies[0] > 500:
            current_preg = self.pregnancies.pop(0)
            sigma = (current_preg - 1) / (12 ** 0.5)
            mu = (self.min+self.max)/2 * current_preg
            new_children = round(np.random.normal(mu, sigma, 1)[0])
            self.new_babies += new_children
        else:
            for each in range(0, self.pregnancies.pop(0)):
                new_children = randint(1, 14)
                self.new_babies += new_children

    def calc_gender_totals(self):
        # This calculates the total number of males and females in the rabbit list
        self.males = 0
        self.females = 0
        if len(self.list) < 49:
            for generation in self.list:
                self.males += (generation['Males'])
                self.females += (generation['Females'])
        else:
            for generation in self.list:
                self.males += generation['Males'] + self.vulnerable_males
                self.females += generation['Females'] + self.vulnerable_females

    def pregnant_rabbits(self):
        # This calculates the number of rabbits that can be pregnant and returns a number of rabbits who become pregnant
        # Rabbits - 2 Month old Rabbits - 1 Month old Rabbits - (Pregnant Females) - (Females who have given birth)
        fertile_males = self.males - self.list[0]['Males'] - self.list[1]['Males']
        fertile_females = self.females - self.list[0]['Females'] - self.list[1]['Females'] - self.pregnancies[0]
        potential_pregnancies = min(fertile_females, fertile_males)
        n, p = potential_pregnancies, self.pregnancy_chance
        num_pregnancies = np.random.binomial(n, p, 1)[0]
        self.pregnancies.append(num_pregnancies)
        return num_pregnancies

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
                        self.deaths_total += 1
            else:
                n, p = self.vulnerable_males, 0.1
                deaths = np.random.binomial(n, p, 1)[0]
                self.vulnerable_males -= deaths
                self.deaths_total += deaths
            deaths = 0
            if self.vulnerable_females < 500:
                for each in range(0, self.vulnerable_females):
                    death_roll = randint(1, 11)
                    if death_roll == 1:
                        deaths += 1
                        self.vulnerable_females -= 1
                        self.deaths_total += 1
            else:
                n, p = self.vulnerable_females, 0.1
                deaths = np.random.binomial(n, p, 1)[0]
                self.vulnerable_females -= deaths
                self.deaths_total += deaths
        

        