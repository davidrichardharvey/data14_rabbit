from rabbit_project.classes.rabbit import Rabbit

test = Rabbit()

def test_pregnant_rabbits():
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



