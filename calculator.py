def add(a, b):
    return a + b


def calculate_total_with_tax(price, tax_rate):
    # Integration: This function calls the 'add' function logic
    return add(price, price * tax_rate)


# Intentional messy code for the linter/formatter to catch:
def unused_function():
    pass
