def unique2(l):
    unique_l = []

    for el in l:
        if el not in unique_l:
            unique_l.append(el)

    return unique_l