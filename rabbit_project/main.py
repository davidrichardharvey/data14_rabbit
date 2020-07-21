import time


def time_passing():
    month = 1
    while True:
        print(f"We are in month {month}")
        time.sleep(1)
        month += 1
