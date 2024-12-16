import pytest
from source.calculator import add


import pytest

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (5, 5, 10),
    (-3, -3, -6)
])
def test_add(x, y, expected):
    assert add(x, y) == expected










