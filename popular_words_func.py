def popular_words(text: str, words: list[str]) -> dict:
    result = {}
    for key in words:
        result[key] = text.lower().split(" ").count(key)
    pass
    return result


assert popular_words(
    """When I was One I had just begun When I was Two I was nearly new """,
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test"
print("OK")
