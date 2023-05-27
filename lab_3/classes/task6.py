def is_prime(n):
    foo = True
    prime_check = lambda a: n % a
    for i in range(2, (n//2)+1):
        if prime_check(i) == 0:
            foo = False
            break

    if foo:
        print(n, end=" ")


lis = input().split()

for i in range(len(lis)):
    is_prime(int(lis[i]))

