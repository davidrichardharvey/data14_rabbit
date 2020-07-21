class Rabbits:
    def __init__(self):
        self.total_population = 2
        self.males = {3: 1, 2: 0, 1: 0}
        self.females = {3: 1, 2: 0, 1: 0}

    def total_population(self):
        total_pop = 0
        for i in self.males:
            total_pop += (self.males[i])
        for i in self.females:
            total_pop += (self.females[i])
        self.total_population = total_pop
        return total_pop

testing = Rabbits()

print(testing.total_population)