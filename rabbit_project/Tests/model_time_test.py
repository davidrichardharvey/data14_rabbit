from rabbit_project.rabbit import Rabbit

test = Rabbit()


def test_model_time():
    assert test.advance_time(0) == 1
    assert test.advance_time(60) == 61
    assert test.advance_time(15) == 16
