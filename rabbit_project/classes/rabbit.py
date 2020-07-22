from random import randint
import time as t


class Rabbit:
    def __init__(self):
        self.total_population = 0
        self.males = 1
        self.females = 1
        self.list = self.init_list()
        self.pregnancies = [0, 0]
        self.new_babies = 0
        self.month = 1

    def calculate_total_pop(self):
        total_pop = 0
        for i in range(0, len(self.list)):
            total_pop += (self.list[i]['Males'] + self.list[i]['Females'])
        self.total_population = total_pop
        return total_pop

    def init_list(self):
        new_list = []
        for each in range(0, 57):
            new_list.append({"Males": 0, "Females": 0})
        new_list.append({"Males": 1, "Females": 1})
        new_list.append({"Males": 0, "Females": 0})
        new_list.append({"Males": 0, "Females": 0})
        return new_list

    def assign_genders(self):
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
        self.new_babies = 0
        for each in range(0, self.pregnancies.pop(0)):
            new_children = randint(1, 14)
            self.new_babies += new_children

    def calc_gender_totals(self):
        self.males = 0
        self.females = 0
        for generation in self.list:
            self.males += generation['Males']
            self.females += generation['Females']

    def time_passing(self):
        while True:
            print(f"We are in month {self.month}")
            t.sleep(1)
            self.month += 1
