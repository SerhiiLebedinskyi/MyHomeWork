continuation_value = ["y", "yes", "так", "да"]

start_of_execution = True

while start_of_execution:

    first_num = int(input("Введіть перше число: ").strip())
    second_num = int(input("Введіть друге число: ").strip())
    action_on_numbers = input("Вкажіть дію (+,-,*,/): ").strip()

    if action_on_numbers == "/" and second_num == 0:
        result = "ДІЛЕННЯ НА 0 НЕМОЖЛИВЕ"
    elif action_on_numbers == "/":
        result = first_num / second_num
    elif action_on_numbers == "*":
        result = first_num * second_num
    elif action_on_numbers == "+":
        result = first_num + second_num
    elif action_on_numbers == "-":
        result = first_num - second_num
    else:
        result = "ВВЕДЕНО ДІЮ НАД ЧИСЛАМИ, ЩО НЕ ВХОДИТЬ ДО (+,-,*,/)"

    print(
        f"Перше число: {first_num}\nДія над числами: {action_on_numbers}\nДруге число: {second_num}\nРезультат = {result}"
    )

    user_response = input("Продовжуємо роботу: ")

    if user_response in continuation_value:
        continue
    else:
        start_of_execution = False
