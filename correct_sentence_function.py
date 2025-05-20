def correct_sentence(text: str) -> str:
    text_title = (
        text if text[0].istitle() else text.replace(text[0], text[0].upper(), 1)
    )
    edited_text = text_title if text.endswith(".") else text_title + "."
    return edited_text


assert correct_sentence("greetings, friends") == "Greetings, friends.", "Test1"
assert correct_sentence("hello") == "Hello.", "Test2"
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", "Test3"
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", "Test4"
assert correct_sentence("greetings, friends.") == "Greetings, friends.", "Test5"
print("ОК")
