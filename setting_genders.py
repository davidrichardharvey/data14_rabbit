from random import randint


class GenderAssign:
    def gender_at_birth(self, number_babies=None, male_count=None, female_count=None):
        # Assigns the genders of each baby individually and groups them together
        if number_babies is None:
            number_babies = self.births
        if male_count is None:
            male_count = self.male_count
        if female_count is None:
            female_count = self.female_count
        males = 0
        females = 0
        for baby in range(0, number_babies):
            gender = randint(0,1)
            if gender == 0:
                males += 1
            elif gender == 1:
                females += 1
        self.male_age = {0: males}
        self.female_age = {0: females}
        male_count += males
        female_count += females
        self.male_count = male_count
        self.female_count = female_count
        return [males, females, male_count, female_count]