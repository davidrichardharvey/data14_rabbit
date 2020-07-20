from time import sleep


class Rabbit:
    def __init__(self):
        self.number_males = 1
        self.number_females = 1
        self.total = self.number_males + self.number_females
        self.months = 0
        self.female_age = {3: 1}  # {age: count_with_age}
        self.male_age = {3: 1}

    def _set_initial(self, month=None, num_males=None, num_females=None, male_age=None, female_age=None):
        if not num_males:
            num_males = self.number_males
        if not num_females:
            num_females = self.number_females
        if not month:
            month = self.months
        if not male_age:
            male_age = self.male_age
        if not female_age:
            female_age = self.female_age
        total = num_males + num_females
        self.total = total
        return [total, month, male_age[3], female_age[3]]

    def advance_time(self, months=None):
        sleep(1)
        if not months:
            months = self.months
        months += 1
        self.months = months
        return months
