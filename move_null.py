initial_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

null_list = []
not_null_list = []

for item in initial_list:
    if item == 0:
        null_list.append(item)
    else:
        not_null_list.append(item)

output_list = not_null_list + null_list
pass
