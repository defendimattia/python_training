def narcissistic(value):

    result = 0

    for num in str(value):
        result += int(num) ** len(str(value))

    return result == value
