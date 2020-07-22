class Rabbits:
    def __init__(self):
        self.total_population = 0
        self.males = 0
        self.females = 0
        self.list = self.init_list()

    def calc_pop(self):
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

    def rabbits_dead(self, new_list):
        print(new_list.pop(0)) = rabbits_dead_count
        return new_list.pop(0)
        

testing = Rabbits()
testing.calc_pop()
print(testing.total_population)
testing.rabbits_dead()