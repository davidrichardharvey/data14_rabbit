import time as t


def time_passing():
    month = 1
    while True:
        print(f"We are in month {month}")
        t.sleep(1)
        month += 1