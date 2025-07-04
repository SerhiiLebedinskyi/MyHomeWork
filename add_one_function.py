def add_one(some_list: list[int]) -> list[int]:
    list_to_string = "".join([str(y) for y in some_list])
    add_one_to_number = int(list_to_string) + 1
    result = [int(num) for num in str(add_one_to_number)]
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")
