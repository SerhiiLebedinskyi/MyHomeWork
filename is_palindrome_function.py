import string


def is_palindrome(text: str) -> bool:
    text_list = [
        str(el)
        for el in text.lower()
        if el in string.ascii_letters or el in string.digits
    ]
    left = 0
    right = len(text_list) - 1
    while left < right:
        left += 1
        right -= 1
        if text_list[left] != text_list[right]:
            return False
    return True


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("ОК")
