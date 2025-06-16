def is_even(digit: int) -> bool:
    """Перевірка чи є парним число"""
    result = digit % 2 == 0
    return result


assert is_even(2) == True, "Test1"
assert is_even(5) == False, "Test2"
assert is_even(0) == True, "Test3"
print("OK")
