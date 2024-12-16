from source.discount_calculator import calculate_discount
import pytest


@pytest.fixture
def base_price():
    return 100

@pytest.mark.parametrize("discount_percent, expected", [
    (0, 100), # ללא הנחה - המחיר נשאר 100
    (10, 90), # 10% הנחה - המחיר 90
    (25, 75),# 25% הנחה - המחיר 75
    (50, 50),# 50% הנחה - המחיר 50
    (30, 60),  # שגיאה
    (-10, 110)

])

def test_calculate_discount(base_price, discount_percent, expected):
    assert calculate_discount(base_price, discount_percent) == expected