from rabbit_project.classes.finding_totals import Rabbit


def test_finding_totals():
    rab = Rabbit()
    assert rab.num_males == 1
    assert rab.num_females == 1
    rab.total_population.append({'Males': 2, 'Females': 1})
    rab.calc_gender_totals()
    assert rab.num_males == 3
    assert rab.num_females == 2


test_finding_totals()