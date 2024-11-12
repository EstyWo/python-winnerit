import pytest
test_data = [(1, 5, 6), (10, 5, 15), (1, 0, 1), (20, 40, 60), (10, 500, 510)]

@pytest.mark.parametrize("num_1, num_2, result", test_data)
def test_sum_parameters(num_1, num_2, result):
    assert num_1 + num_2 == result