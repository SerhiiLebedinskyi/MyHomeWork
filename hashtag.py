import string

user_input: str = input("Вкажіть бажане значення hashtag: ").strip().title()

hashtag_list: str = [
    char for char in user_input if char not in string.punctuation and char != " "
]

hashtag_output = "#" + "".join(hashtag_list)

if len(hashtag_output) > 140:
    print(hashtag_output[0:140])
else:
    print(hashtag_output)

pass
