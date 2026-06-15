def move_zeros(lst):
    for i in range(lst.count(0)):
        lst.remove(0)
        lst.append(0)
    return lst