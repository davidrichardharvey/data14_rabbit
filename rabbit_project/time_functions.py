import time as t
from rabbit_project.classes.rabbit import Rabbit


def time_passing(final_month):
    month = 1
    while month <= final_month:
        print(f"We are in month {month}")
        rabbit_one_month()
        print(f"Population: {testing.total_population}")
        print(f"Pregnancies: {testing.pregnancies}")
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



# def rabbit_one_month():
#     print(f"We are in month {month}")
#     testing.pregnant_babies()
#     testing.birth_children()
#     testing.assign_genders()
#     testing.calc_gender_totals()
#     testing.calculate_total_pop()
#     print(f"Population: {testing.total_population}")
#     print(f"Males: {testing.males}")
#     print(f"Females: {testing.females}")

testing = Rabbit()
