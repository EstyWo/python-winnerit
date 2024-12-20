from source.accum import Accumulator
import pytest

def test_accum_creation():
    accum = Accumulator()
    assert accum.count == 0

@pytest.mark.api
def test_add_counts_twice():
    accum = Accumulator()
    accum.add_counts()
    accum.add_counts()
    assert accum.count == 2

@pytest.mark.ui
def test_add_counts_with_params(global_accum):
    global_accum.add_counts(10)
    assert global_accum.count == 10