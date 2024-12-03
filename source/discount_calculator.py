#discount_calculator

def calculate_discount(price, discount_percent):
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be non-negative")
    return price * (1 - discount_percent / 100)