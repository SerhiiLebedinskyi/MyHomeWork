import string
import keyword

MY_STRING_PUNCTUATION = "!\"#$%&'()*+, -./:;<=>?@[\\]^`{|}~"

valid_list = []
is_valid = None

# input block
string_to_be_checked = input("Введіть бажану назву змінної: ").strip()

# check block
if len(string_to_be_checked) > 0:
    valid_list.append(string_to_be_checked not in keyword.kwlist)
    valid_list.append(string_to_be_checked[0] not in string.digits)
    valid_list.append(
        string_to_be_checked.islower() and string_to_be_checked.count("_") <= 1
    )
    valid_list.append(
        all([char not in MY_STRING_PUNCTUATION for char in string_to_be_checked])
    )
    is_valid = all(valid_list)
else:
    is_valid = False

print(is_valid)
pass
