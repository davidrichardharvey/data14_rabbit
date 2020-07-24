from rabbit_project.classes.rabbit import Rabbit
from scipy import stats

test = Rabbit()

def test_pregnant_rabbits():
<<<<<<< HEAD:rabbit_project/tests/test_pregnant_rabbits.py
    assert test.males == 1
    assert test.females == 1
    assert test.pregnancies == [0, 1]
    assert stats.binom_test(test.pregnancies, test.females, 0.5, 'two-sided')

=======
    test.pregnant_rabbits()
    assert test.pregnancies == [0, 1, 0]

    test.males = 60
    test.females = 60
    test.list = []
    for each in range(0, 60):
        test.list.append({"Males": 1, "Females": 1})
    test.pregnancies = [0, 0]
    test.pregnant_rabbits()
    assert test.pregnancies == [0, 0, 58]

    test.males = 60
    test.females = 600
    test.list = []
    for each in range(0, 60):
        test.list.append({"Males": 1, "Females": 10})
    test.pregnancies = [0, 0]
    test.pregnant_rabbits()
    assert test.pregnancies == [0, 0, 580]

    test.males = 60
    test.females = 1200
    test.list = []
    for each in range(0, 60):
        test.list.append({"Males": 1, "Females": 20})
    test.pregnancies = [0, 0]
    test.pregnant_rabbits()
    assert test.pregnancies == [0, 0, 580]

    test.males = 240
    test.females = 60
    test.list = []
    for each in range(0, 60):
        test.list.append({"Males": 4, "Females": 1})
    test.pregnancies = [0, 0]
    test.pregnant_rabbits()
    assert test.pregnancies == [0, 0, 58]
>>>>>>> dev:rabbit_project/tests/test_pregnant__rabbits.py



