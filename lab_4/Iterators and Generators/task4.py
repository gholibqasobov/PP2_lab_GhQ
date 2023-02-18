def squares(a, b):
    while a <= b:
        yield a ** 2
        a += 1


a = int(input('Enter the startpoint: '))
b = int(input('Enter the endpoint: '))

for i in squares(a, b):
    print(i)


