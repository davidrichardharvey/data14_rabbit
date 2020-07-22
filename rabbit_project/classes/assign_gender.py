from random import randint


class Rabbit:
    def __init__(self):
        self.pregnancies = [0, 0]
        self.new_babies = 0
        self.total_population = []

    def assign_genders(self):
        males = 0
        females = 0
        for baby in range(0, self.new_babies):
            gender = ['M', 'F'][randint(0, 1)]
            if gender == 'M':
                males += 1
            elif gender == 'F':
                females += 1
        self.total_population.append({'Males': males, 'Females': females})
