def spy_game(l):
    first_zero = l.index(0)
    second_zero = l.index(0, first_zero + 1)  # index(el, start, end)
    seven = l.index(7)
    if l[first_zero:second_zero] != seven and seven > second_zero:
        return True

    return False

print(spy_game([1,0,2,0,4,5,7]))
