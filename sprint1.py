class Rabbit:
    def __init__(self):
        self.number_males = 1
        self.number_females = 1
        self.total = self.number_males + self.number_females
        self.months = 0

    def _set_initial(self, month=None, num_males=None, num_females=None):
        if not num_males:
            num_males = self.number_males
        if not num_females:
            num_females = self.number_females
        if not month:
            month = self.months
        total = num_males + num_females
        self.total = total
        return [total, month]

xyz = Rabbit()
print(xyz._set_initial())