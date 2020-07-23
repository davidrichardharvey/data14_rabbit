import time as t
import csv
from rabbit_project.classes.rabbit import Rabbit

rabbit_population_model = Rabbit()

# model_count = 0

def time_passing(final_month):
    create_rabbit_csv()
    month = 1
    while month <= final_month:
        print(f"We are in month {month}")
        rabbit_one_month()
        append_data_csv(month, rabbit_population_model.total_population,
                        rabbit_population_model.males, rabbit_population_model.females,
                        rabbit_population_model.deaths_total)
        print(rabbit_population_model.pregnancies)
        print(f"Population: {rabbit_population_model.total_population}")
        print(f"Deaths: {rabbit_population_model.deaths_total}")
        print(f"Males: {rabbit_population_model.males}")
        print(f"Females: {rabbit_population_model.females}\n")
        t.sleep(1)
        month += 1
    # model_count += 1



def rabbit_one_month():
    rabbit_population_model.pregnant_rabbits()
    rabbit_population_model.birth_children()
    rabbit_population_model.assign_genders()
    rabbit_population_model.calc_gender_totals()
    rabbit_population_model.rabbits_dead()
    rabbit_population_model.calculate_total_pop()
    append_data_csv(month, rabbit_population_model.total_population,
                    rabbit_population_model.males, rabbit_population_model.females, rabbit_population_model.deaths_total)


def append_data_csv(month, total_population, males, females, deaths):
    # Appends new month data to a csv file
    with open("rabbit_modelling_data", "a") as rabbit_data:
        csv_append = csv.writer(rabbit_data)
        csv_append.writerow([month, total_population, males, females, deaths])

