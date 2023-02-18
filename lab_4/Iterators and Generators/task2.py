def even(n):
    i = 2
    if n < 2:
        yield 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


n = int(input('Enter the range: '))
l = [i for i in even(n)]
for i in range(len(l)):
    if i != len(l) - 1:
        print(l[i], end=', ')
    else:
        print(l[i])
