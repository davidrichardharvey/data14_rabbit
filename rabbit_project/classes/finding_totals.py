class Rabbit:
    def __init__(self):
        self.total_population = [{'Males': 1, 'Females': 1}]
        self.males = 1
        self.females = 1

    def calc_gender_totals(self):
        self.males = 0
        self.females = 0
        for generation in self.total_population:
            self.males += generation['Males']
            self.females += generation['Females']