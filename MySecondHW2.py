user_name = input("Введіть ваше ім'я:")
user_numeric = int(input(f"{user_name}, введіть 4-х значне число:"))
div1000, mod1000 = divmod(user_numeric, 1000)
print(div1000)
div100, mod100 = divmod(mod1000, 100)
print(div100)
div10, mod10 = divmod(mod100, 10)
print(div10)
print(mod10)
