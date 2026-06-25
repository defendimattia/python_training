def persistence(n):

    counter = 0

    while n >= 10:

        nums = [int(num) for num in str(n)]
        new_n = 1

        for i in nums:
            new_n *= i

        n = new_n

        counter += 1

    return counter
