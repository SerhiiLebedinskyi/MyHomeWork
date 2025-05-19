def common_elements() -> set:
    multiples_of_3 = {elem for elem in range(100) if elem % 3 == 0}
    multiples_of_5 = {elem for elem in range(100) if elem % 5 == 0}
    result = multiples_of_3 & multiples_of_5
    return result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
