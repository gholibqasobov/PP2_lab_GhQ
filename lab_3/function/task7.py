l = list(input().split())


# l = list(l.split())


def consqutiv_three(l):
    foo = False
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            if int(l[i]) == 3:
                foo = True
                break

    return foo


print(consqutiv_three(l))
