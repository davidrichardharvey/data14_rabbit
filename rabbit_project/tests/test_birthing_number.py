from rabbit_project.classes.rabbit import Rabbit


def test_birth_children():
    test = Rabbit()
    assert test.pregnancies == [0, 1]  # Assert assumes that variable is already set as that number
    test.birth_children()
    assert test.new_babies == 0
    test.pregnancies = [0, 5]
    test.birth_children()
    assert test.new_babies == 0
    test.pregnancies = [7, 0]
    test.birth_children()
    assert 7 <= test.new_babies <= 98
    test.pregnancies = [10, 8]
    test.birth_children()
    assert 10 <= test.new_babies <= 140

test_birth_children()

