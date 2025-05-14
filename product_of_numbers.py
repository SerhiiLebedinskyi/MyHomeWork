number_input = int(input("Введіть число: ").strip())

num = number_input

while num >= 10:
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    num = product

print(num)
