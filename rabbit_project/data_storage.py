import csv
# from time_functions import the time function

class RabbitCsv:

    def __init__(self):
        self.headers_list = ["Months", " Total Population",
                    " Males", " Females", " Deaths"]
        self.model_count = 1
        self.model_print = [f"Model {model_count}:"]
        self.list_for_csv = []


    def create_rabbit_csv(self):
        with open("rabbit_modelling_data", "w") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(model_print)
            csv_writer.writerow(headers_list)


    def append_data_csv(self):
        with open("rabbit_modelling_data", "a") as rabbit_data:
            csv_append = csv.writer(rabbit_data)
            # Refactor monthly outputs into list of lists --> talk to Alex & other devs
            csv_append.writerow(list_for_csv)

    def advance_model(self):
        with open("rabbit_modelling_data", "a") as model_move:
            
            # model_count += 1
            # csv_append.writerow(model_print)
            # csv_append.writerow(headers_list)

    create_rabbit_csv()
    # model_count += 1
    # append_data_csv()

# Code to be added to the time function:

# list_for_csv.append [month, total_population, males, females, deaths]

