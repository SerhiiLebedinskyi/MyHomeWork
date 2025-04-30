initial_list = [1, 2, 3]
length_initial = len(initial_list)
if length_initial == 0:
    first_list = second_list = initial_list
else:
    half_length_initial = length_initial // 2
    if length_initial % 2 == 0:
        first_list = initial_list[:half_length_initial]
        second_list = initial_list[half_length_initial:]
    elif length_initial % 2 != 0:
        first_list = initial_list[: half_length_initial + 1]
        second_list = initial_list[half_length_initial + 1 :]

output_list = [first_list, second_list]
pass
