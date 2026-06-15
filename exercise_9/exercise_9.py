def digital_root(n):

    while n > 9:
        n = sum(int(num) for num in str(n))

    return n
