from time import sleep


class AgingUp:
    def __init__(self):
        self.months = 0
        self.male_age = {3: 1}
        self.female_age = {3: 1}
        self.males_born = 0
        self.females_born = 0

    def advance_time(self, months_since_start=None, male_age=None, female_age=None, males_born=None,
                     females_born=None):
        # Increases the months attribute by 1 and increases the key for male and female ages
        sleep(1)
        if months_since_start is None:
            months_since_start = self.months
        if male_age is None:
            male_age = self.male_age
        if female_age is None:
            female_age = self.female_age
        if males_born is None:
            males_born = self.males_born
        if females_born is None:
            females_born = self.females_born
        new_male_dict = {}
        new_female_dict = {}
        for age in male_age:
            new_male_dict[age + 1] = male_age[age]
        for age in female_age:
            new_female_dict[age + 1] = female_age[age]
        new_male_dict[0] = males_born
        new_female_dict[0] = females_born
        male_age = new_male_dict
        female_age = new_female_dict
        self.male_age = male_age
        self.female_age = female_age
        months_since_start += 1
        self.months = months_since_start
        return [months_since_start, male_age, female_age]


test = AgingUp()
test.advance_time(1, {3: 1}, {3: 1}, 6, 2)
print(test.male_age)
