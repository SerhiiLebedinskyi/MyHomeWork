def is_even(digit):
    """Перевірка чи є парним число"""
    result = True if digit % 2 == 0 else False
    return result


assert is_even(2) == True, "Test1"
assert is_even(5) == False, "Test2"
assert is_even(0) == True, "Test3"
print("OK")
