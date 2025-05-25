def find_unique_value(some_list: list) -> int:
    meets_once, several_times = set(), set()

    for value in some_list:
        if value in several_times:
            continue
        if value in meets_once:
            meets_once.remove(value)
            several_times.add(value)
        else:
            meets_once.add(value)
    result = meets_once.pop()
    return result


assert find_unique_value([1, 2, 1, 1]) == 2, "Test1"
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, "Test2"
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, "Test3"
print("ОК")
