import random

MIN = 3
MAX = 10
size_list = random.randint(MIN, MAX) + 1

random_list = []
output_list = []

for i in range(1, size_list):
    random_list.append(i)

output_list.append(random_list[0])
output_list.append(random_list[2])
output_list.append(random_list[len(random_list) - 2])
pass
