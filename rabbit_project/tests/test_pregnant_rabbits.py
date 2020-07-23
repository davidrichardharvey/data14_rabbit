from rabbit_project.classes.rabbit import Rabbit
from scipy import stats

test = Rabbit()

def test_pregnant_rabbits():
    assert test.males == 1
    assert test.females == 1
    assert test.pregnancies == [0, 1]
    assert stats.binom_test(test.pregnancies, test.females, 0.5, 'two-sided')




