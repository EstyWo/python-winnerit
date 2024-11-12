import pytest


def test_by_zero():
    num = 2 / 0

def test_division_by_zero():
    with pytest.raises(Exception) as e:
        num = 2 / 0

    assert str(e.value) in 'division by zero'
    assert str(e.typename) in 'ZeroDivisionError'