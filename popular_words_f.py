def popular_words(text: str, words: list[str]) -> dict:
    words_list_lower = text.lower().split("")
    result = {}
    for key in words:
        result[key] = words_list_lower.count(key)
    return result


assert popular_words(
    """When I was One I had just begun When I was Two I was nearly new """,
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test"
print("OK")
