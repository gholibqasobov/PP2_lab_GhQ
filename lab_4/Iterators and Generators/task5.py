def down(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input('Enter the range: '))
for i in down(n):
    print(i)