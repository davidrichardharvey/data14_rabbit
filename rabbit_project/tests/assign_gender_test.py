import pytest
from assign_gender import Rabbit


def test_assign_gender():
    roger = Rabbit()
    # Given inputs for testing
    roger.total_population = [{'Males': 1, 'Females': 1}, {'Males': 0, 'Females': 0},
                              {'Males': 0, 'Females': 0}, {'Males': 2, 'Females': 3},
                              {'Males': 0, 'Females': 0}]
    roger.new_babies = 12
    roger.assign_genders()
    # Test to ensure previous data has not been modified
    assert roger.total_population[0:-1] == [{'Males': 1, 'Females': 1}, {'Males': 0, 'Females': 0},
                                      {'Males': 0, 'Females': 0}, {'Males': 2, 'Females': 3},
                                      {'Males': 0, 'Females': 0}]
    # Tests to check assigned genders are equal to number of babies
    assert 0 <= roger.total_population[-1]['Males'] <= 12
    assert roger.total_population[-1]['Males'] + roger.total_population[-1]['Females'] == 12
    # Tests to ensure that outputs are not none
    roger.assign_genders()
    assert roger.total_population[-1]['Males'] is not None
    assert roger.total_population[-1]['Females'] is not None


test_assign_gender()
