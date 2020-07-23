import time as t
from rabbit_project.classes.rabbit import Rabbit
import pytest

def test_time_passing():
    month = 1
    final_month = 10
    assert month == 1
    assert month <= final_month
    final_month = 1
    assert month <= final_month
    while month <= final_month:
        # print(f"We are in month {month}")
        # rabbit_one_month()
        # print(f"Population: {testing.total_population}")
        # print(f"Pregnancies: {testing.pregnancies}")
        # print(f"Males: {testing.males}")
        # print(f"Females: {testing.females}\n")
        t.sleep(0.5)
        month += 1
