from advance_time_refactored import AgingUp
import pytest

time_test = AgingUp()



def test_advance_time():
    # Inputs - (months since start, male age,
    # female age, males born, females born)
    # Output - [months_since_start, male_age, female_age]

    # Testing that months increases by one
    assert time_test.advance_time(1, {1: 5}, {1: 2}, 3, 5)[0] == 2

    # Testing that male age increases by one
    assert time_test.advance_time(5, {0: 0, 1: 6, 2: 3, 3: 4, 4: 2}, {0: 3, 1: 8, 2: 2, 3: 1, 4: 1},
                                  4, 1)[1] == {0: 4, 1: 1, 2: 6, 3: 3, 4: 4, 5: 2}

    # Testing that female age increases by one
    assert time_test.advance_time(7, {0: 3, 1: 2, 2: 5, 3: 7, 4: 0, 5: 10, 6: 5}, {0: 1, 1: 5, 2: 4, 3: 1, 4: 12, 5: 6, 6: 2},
                                  14, 16)[2] == {0: 16, 1: 3, 2: 2, 3: 5, 4: 7, 5: 0, 6: 10, 7: 5}

    # Testing outputs are not none



