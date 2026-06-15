def duplicate_count(text):
    return sum(1 for char in set(text.lower()) if text.lower().count(char) > 1)
