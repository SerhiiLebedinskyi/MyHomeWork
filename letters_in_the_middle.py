import string

all_letters = string.ascii_letters
interval: str = input(
    "Введіть дві літери розділивши їх дефісом, наприклад (а-А):"
).strip()
start = all_letters.index(interval[0])
finish = all_letters.index(interval[-1]) + 1
print(all_letters[start:finish])
