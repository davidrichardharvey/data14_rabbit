# As a modeler I want 1 month to be equal to one second
# so that i can track the number of rabbits with time
from sprint1 import Rabbit
test = Rabbit()

def test_number_of_babies():
    assert 10 <= test.number_of_babies(10) <= 140
    assert 1 <= test.number_of_babies(1) <= 14
    assert test.number_of_babies(0) == 0