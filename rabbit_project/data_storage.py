import csv
# from time_functions import the time function

def create_rabbit_csv():
    headers_list = ["Months", " Total Population",
                    " Males", " Females", " Deaths"]
    model_start = ["Model One:"]
    with open("rabbit_modelling_data", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(model_start)
        csv_writer.writerow(headers_list)

# create_rabbit_csv()

def append_data_csv():
    with open("rabbit_modelling_data", "a") as new_file:
        csv_append = csv.writer(new_file)
        # Refactor monthly outputs into list of lists --> talk to Alex & other devs
        csv_append.writerows(list_for_csv)

# Code to be added to the time function:
# list_for_csv = []
# list_for_csv.append [month, total_population, males, females, deaths]

