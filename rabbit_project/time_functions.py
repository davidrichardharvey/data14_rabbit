import time as t
from rabbit_project.classes.rabbit import Rabbit

rabbit_population_model = Rabbit()


def time_passing(final_month):
    month = 1
    while month <= final_month:
        print(f"We are in month {month}")
        rabbit_one_month()
        print(f"Population: {rabbit_population_model.total_population}")
        print(f"Deaths: {rabbit_population_model.deaths_total}")
        print(f"Males: {rabbit_population_model.males}")
        print(f"Females: {rabbit_population_model.females}\n")
        t.sleep(1)
        month += 1


def rabbit_one_month():
    rabbit_population_model.pregnant_rabbits()
    rabbit_population_model.birth_children()
    rabbit_population_model.assign_genders()
    rabbit_population_model.calc_gender_totals()
    rabbit_population_model.rabbits_dead()
    rabbit_population_model.calculate_total_pop()

