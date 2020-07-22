import csv


def create_rabbit_csv():
    headers_list = ["Months", " Total Population",
                    " Males", " Females", " Deaths"]
    with open("rabbit_modelling_data", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers_list)


def append_data_csv():
    with open("rabbit_modelling_data", "a") as new_file:
        csv_append = csv.writer(new_file)
        # Refactor monthly outputs into list of lists --> talk to Alex & other devs
        csv_append.writerows(list_for_csv)

list_for_csv = []
list_for_csv.append [month, total_population, males, females, deaths]

