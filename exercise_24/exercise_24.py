def to_camel_case(text):

    refactored_text = text.replace("_", "-").split("-")

    return refactored_text[0] + "".join(
        [word.capitalize() for word in refactored_text[1:]]
    )
