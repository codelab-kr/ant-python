import pytest
from memoization.main import AntSequence

def test_get_ln():
    ant = AntSequence()
    assert ant.get_ln(4) == '1211'
    assert ant.get_ln(5) == '111221'
    assert ant.get_ln(6) == '312211'
    assert ant.get_ln(7) == '13112221'
    assert ant.get_ln(8) == '1113213211'

def test_get_m():
    ant = AntSequence()
    assert ant.get_m(4) == '21'
    assert ant.get_m(5) == '12'
    assert ant.get_m(6) == '22'
    assert ant.get_m(7) == '12'
    assert ant.get_m(8) == '21'