from rabbit_project.classes.birthing_number import Rabbits

test = Rabbits()

def test_birth_children():
    assert test.pregnancies[0] == 0  # Assert assumes that variable is already set as that number
    test.birth_children()
    assert test.new_babies == 0
    test.pregnancies[0] = 1
    test.birth_children()
    assert 1 <= test.new_babies <= 14
    test.pregnancies[0] = 10
    test.birth_children()
    assert 10 <= test.new_babies <= 140

