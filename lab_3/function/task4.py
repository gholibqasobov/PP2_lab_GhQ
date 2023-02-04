l = list((input().split(" ")))


def is_prime(n):
    foo = True
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            foo = False
            break

    if foo:
        print(n, end=" ")


for i in range(len(l)):
    is_prime(int(l[i]))
