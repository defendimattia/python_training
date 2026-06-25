alp = "abcdefghijklmnopqrstuvwxyz"


def alphabet_position(text):

    return " ".join(
        str(alp.index(letter) + 1) for letter in text.lower() if letter in alp
    )
