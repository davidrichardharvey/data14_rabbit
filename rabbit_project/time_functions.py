import time as t
import csv
from rabbit_project.classes.rabbit import Rabbit
import os

rabbit_population_model = Rabbit()


def time_passing(final_month):
    model_count = 1
    while os.path.isfile(f"rabbit_modelling_data{model_count}.csv"):
        model_count += 1
    create_rabbit_csv(model_count)
    month = 1
    year = 0
    rem_month = month
    while month <= final_month:
        print(f"We are in year {year} month {rem_month}")
        rabbit_one_month()
        print(f"Population: {rabbit_population_model.total_population:,d}")
        print(f"Deaths: {rabbit_population_model.deaths_total:,d}")
        print(f"Males: {rabbit_population_model.males:,d}")
        print(f"Females: {rabbit_population_model.females:,d}\n")
        append_data_csv(year, rem_month, rabbit_population_model.total_population,
                        rabbit_population_model.males, rabbit_population_model.females,
                        rabbit_population_model.deaths_total, model_count)

        t.sleep(1)
        month += 1
        year = int(month/12)
        rem_month = month % 12


def rabbit_one_month():
    rabbit_population_model.pregnant_rabbits()
    rabbit_population_model.birth_children()
    rabbit_population_model.assign_genders()
    rabbit_population_model.calc_gender_totals()
    rabbit_population_model.calculate_total_pop()


def append_data_csv(year, rem_month, total_population, males, females, deaths, model_count):
    # Appends new month data to a csv file
    with open(f"rabbit_modelling_data{model_count}.csv", "a", newline="") as rabbit_data:
        csv_append = csv.writer(rabbit_data)
        csv_append.writerow([year, rem_month, total_population, males, females, deaths])


def create_rabbit_csv(model_count):
    headers_list = ["Year", "Month", "Total Population",
                    "Males", "Females", "Deaths"]
    with open(f"rabbit_modelling_data{model_count}.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers_list)


