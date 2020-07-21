import pytest

from setting_genders import GenderAssign

instance = GenderAssign()

def test_gender_at_birth():
    # Testing gender assignment numbers are valid
    assert instance.gender_at_birth(13, 5, 1)[0] >= 0
    assert instance.gender_at_birth(7, 1, 1)[0] <= 7
    assert instance.gender_at_birth(4, 5, 2)[1] >= 0
    assert instance.gender_at_birth(6, 2, 3)[1] <= 6
    assert instance.gender_at_birth(10, 4, 3)[2] >= 4
    assert instance.gender_at_birth(16, 3, 2)[2] <= 19
    assert instance.gender_at_birth(9, 5, 2)[3] >= 2
    assert instance.gender_at_birth(22, 8, 3)[3] <= 25
    # Testing outputs when there are no births
    assert instance.gender_at_birth(0, 4, 5)[0] == 0
    assert instance.gender_at_birth(0, 2, 3)[1] == 0
    assert instance.gender_at_birth(0, 6, 7)[2] == 6
    assert instance.gender_at_birth(0, 6, 9)[3] == 9
    # Ensuring outputs are not none
    assert instance.gender_at_birth(13, 3, 2)[0] is not None
    assert instance.gender_at_birth(27, 5, 4)[1] is not None
    assert instance.gender_at_birth(19, 6, 2)[2] is not None
    assert instance.gender_at_birth(9, 3, 1)[3] is not None

