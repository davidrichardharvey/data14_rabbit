import pytest
from rabbit_project.classes.rabbit import Rabbit

def test_assign_gender():
    roger = Rabbit()
    # Given inputs for testing
    roger.list = [{'Males': 1, 'Females': 1}, {'Males': 0, 'Females': 0},
                              {'Males': 0, 'Females': 0}, {'Males': 2, 'Females': 3},
                              {'Males': 0, 'Females': 0}]
    roger.new_babies = 12
    roger.assign_genders()
    # Test to ensure previous data has not been modified
    assert roger.list[1:] == [{'Males': 1, 'Females': 1}, {'Males': 0, 'Females': 0},
                                      {'Males': 0, 'Females': 0}, {'Males': 2, 'Females': 3},
                                      {'Males': 0, 'Females': 0}]
    # Tests to check assigned genders are equal to number of babies
    # Test to see that values are within the valid range
    assert 0 <= roger.list[0]['Males'] <= 12
    assert roger.list[0]['Males'] + roger.list[0]['Females'] == 12
    # Tests to ensure that outputs are not none
    roger.assign_genders()
    assert roger.list[0]['Males'] is not None
    assert roger.list[0]['Females'] is not None

