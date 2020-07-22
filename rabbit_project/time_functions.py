import time as t
from rabbit_project.classes.rabbit import Rabbit


def time_passing():
    month = 1
    while True:
        print(f"We are in month {month}")
        testing.pregnant_babies()
        testing.birth_children()
        testing.assign_genders()
        testing.calc_gender_totals()
        testing.calculate_total_pop()
        print(f"Population: {testing.total_population}")
        print(f"Males: {testing.males}")
        print(f"Females: {testing.females}")
        t.sleep(1)
        month += 1


testing = Rabbit()


time_passing()
