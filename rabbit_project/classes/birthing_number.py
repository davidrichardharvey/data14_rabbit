from random import randint


class Rabbits:
    def __init__(self):
        self.pregnancies = [0, 0]  # [ready_to_birth, new_pregnancies]
        self.new_babies = 0

    def birth_children(self):
        self.new_babies = 0
        for each in range(0, self.pregnancies.pop(0)):
            new_children = randint(1, 14)
            self.new_babies += new_children
