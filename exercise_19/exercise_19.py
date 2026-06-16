import string

def rot13(message):
    result = ""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    for c in message:
        if c in lower:
            result += lower[(lower.index(c) + 13) % 26]
        elif c in upper:
            result += upper[(upper.index(c) + 13) % 26]
        else:
            result += c
    
    return result