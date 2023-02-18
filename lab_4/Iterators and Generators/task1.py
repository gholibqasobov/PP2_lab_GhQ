def sqr(N):
    i = 1
    while i <= N:
        yield i ** 2
        i += 1


N = int(input('Enter the range: '))

for sq in sqr(N):
    print(sq)
