from rabbit_project.classes.rabbits import Rabbits


def test_initial_breeding_pair():
    assert Rabbits().num_male == 1
    assert Rabbits().num_female == 1
