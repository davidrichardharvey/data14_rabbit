import pytest
from ..classes.rabbit import Rabbit


def test_rabbit_init():
    r = Rabbit()
    assert r.males == 1
    assert r.females == 1
    r.calculate_total_pop()
    assert r.total_population == r.males + r.females
