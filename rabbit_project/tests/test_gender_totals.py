from rabbit_project.classes.rabbit import Rabbit


def test_finding_totals():
    rab = Rabbit()
    assert rab.males == 1
    assert rab.females == 1
    rab.total_population.append({'Males': 2, 'Females': 1})
    rab.calc_gender_totals()
    assert rab.males == 3
    assert rab.females == 2


test_finding_totals()