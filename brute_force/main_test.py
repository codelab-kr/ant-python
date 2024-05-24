import pytest
from brute_force.main import AntSequence

def test_get_ln():
    ant = AntSequence()
    assert ant.get_ln() == '11'
    assert ant.get_ln() == '21'
    assert ant.get_ln() == '1211'
    assert ant.get_ln() == '111221'
    assert ant.get_ln() == '312211'
    assert ant.get_ln() == '13112221'
    assert ant.get_ln() == '1113213211'
    

def test_repeat():
    ant = AntSequence()
    assert ant.repeat(4) == '1211'
    assert ant.repeat(5) == '111221'
    assert ant.repeat(6) == '312211'
    assert ant.repeat(7) == '13112221'
    assert ant.repeat(8) == '1113213211'    
    

def test_get_m():
    ant = AntSequence()
    assert ant.get_m(4) == '21'
    assert ant.get_m(5) == '12'
    assert ant.get_m(6) == '22'
    assert ant.get_m(7) == '12'
    assert ant.get_m(8) == '21'
    