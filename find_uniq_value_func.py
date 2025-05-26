def find_unique_value(some_list: list) -> int:
    transformation_set = set(some_list)
    for value in transformation_set:
        if some_list.count(value) == 1:
            break
    result = value
    return result


assert find_unique_value([1, 2, 1, 1, 3]) == 2, "Test1"
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, "Test2"
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, "Test3"
print("ОК")
