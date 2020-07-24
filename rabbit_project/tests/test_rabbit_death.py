from rabbit_project.classes.rabbit import Rabbit
from scipy import stats

test = Rabbit()

def test_rabbits_dead_new():
    assert test.list == test.init_list()
    assert test.deaths_total == 0  # Checking deaths from initial list

    test.list = []
    for i in range(0, 49):
        test.list.append({"Males": 20, "Females": 20}) # Resetting list so we can test input figures

    test.rabbit_deaths_new()
    assert test.deaths_total in range(0, 41)  # Tests that the range of deaths is within viable boundaries

    test.list = []
    for i in range(0, 49):
        test.list.append({"Males": 0, "Females": 20})

    test.rabbit_deaths_new()
    assert test.deaths_total in range(0, 21)

    test.list = []
    for i in range(0, 49):
        test.list.append({"Males": 1000, "Females": 0})  # Resests list and has values that allow us to test binomial

    test.rabbit_deaths_new()
    assert stats.binom_test(test.deaths_total, test.vulnerable_males, 0.1, 'two-sided')  # Tests that the binomial calcs work properly

    test.list = []
    for i in range(0, 49):
        test.list.append({"Males": 0, "Females": 1000})

    test.rabbit_deaths_new()
    assert stats.binom_test(test.deaths_total, test.vulnerable_females, 0.1, 'two-sided')



