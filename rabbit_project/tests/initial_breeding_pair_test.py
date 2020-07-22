from rabbit_project.classes.rabbit import Rabbit


def test_initial_breeding_pair():
    rab = Rabbit()
    assert rab.males == 1
    assert rab.females == 1

test_initial_breeding_pair()