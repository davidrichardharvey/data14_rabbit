from rabbit_project.classes.rabbit_death import Rabbits

test = Rabbits()

def test_rabbits_dead():
    assert test.list == test.init_list()
    test.rabbits_dead()
    assert test.deaths_total == 0  # Checking deaths from initial list

    test.list = []
    for i in range(0, 60):
        test.list.append({"Males": 3, "Females": 9})
    test.rabbits_dead()
    assert test.deaths_total == 12  # Checking total deaths from a made up list
    assert len(test.list) == 59  # Checking the list has been shortened by 1 element

    test.list = []
    for i in range(0, 60):
        test.list.append({"Males": 0, "Females": 4})
    test.rabbits_dead()
    assert test.deaths_total == 16  # Checking total deaths when added on previous total deaths


