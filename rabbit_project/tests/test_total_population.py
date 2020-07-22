from rabbit_project.classes.rabbit import Rabbit


def test_calculate_total_pop():
    r = Rabbit()
    r.list = r.init_list()
    assert r.calculate_total_pop() == 2
    r.list = [{"Males": 0, "Females":0}]
    assert r.calculate_total_pop() == 0
    r.list = [{"Males": 1, "Females":1}]
    assert r.calculate_total_pop() == 2
    r.list = [{"Males": 10, "Females":9},{"Males": 17, "Females":22}]
    assert r.calculate_total_pop() == 58

test_calculate_total_pop()