from rabbit_project.classes.rabbit import Rabbit

test = Rabbit()

def test_pregnant_rabbits():
    assert test.males == 1
    assert test.females == 1
    assert test.pregnancies == [0, 1]
    # assert test.pregnant_babies() == 1



