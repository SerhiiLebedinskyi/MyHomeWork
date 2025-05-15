# converting a number to time

# block input
input_number = int(input("Введіть число, яке потрібно перетворити в час: ").strip())

# block converting
number_of_minutes, number_of_seconds = divmod(input_number, 60)
number_of_hours, number_of_minutes = divmod(number_of_minutes, 60)
number_of_days, number_of_hours = divmod(number_of_hours, 24)

time_dict = {
    "days": number_of_days,
    "hours": number_of_hours,
    "minutes": number_of_minutes,
    "seconds": number_of_seconds,
}

if time_dict["days"] % 100 != 11 and time_dict["days"] % 10 == 1:
    result = "день"
elif 5 > time_dict["days"] % 10 > 1 and time_dict["days"] % 100 not in [12, 13, 14]:
    result = "дні"
else:
    result = "днів"

# block output
time_string = (
    str(time_dict["days"])
    + f" {result}, "
    + str(time_dict["hours"]).zfill(2)
    + ":"
    + str(time_dict["minutes"]).zfill(2)
    + ":"
    + str(time_dict["seconds"]).zfill(2)
)

print(time_string)
