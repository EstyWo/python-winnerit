import pytest
from source.accum import Accumulator
# from source.calculator import


@pytest.fixture
def sample_data():
    return {"name": "pytest", "version": 7.1}


@pytest.fixture (scope = "function")
def global_accum():
    return Accumulator()

# @pytest.fixture()
# def base_price():
#     return 100