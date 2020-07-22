import time as t
from rabbit_project.classes.rabbit import Rabbit

testing = Rabbit()


def time_passing():
    month = 1
    while True:
        print(f"We are in month {month}")
        rabbit_one_month()
        print(f"Population: {testing.total_population}")
        print(f"Deaths: {testing.deaths_total}")
        print(f"Males: {testing.males}")
        print(f"Females: {testing.females}\n")
        t.sleep(1)
        month += 1


def rabbit_one_month():
    testing.pregnant_babies()
    testing.birth_children()
    testing.assign_genders()
    testing.calc_gender_totals()
    testing.calculate_total_pop()


