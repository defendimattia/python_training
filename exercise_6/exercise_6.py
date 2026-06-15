def high_and_low(numbers):

    list = [int(x) for x in numbers.split()]

    return f"{max(list)} {min(list)}"
