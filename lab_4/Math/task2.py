h = int(input('Height: '))
a = int(input('Base, first value: '))
b = int(input('Base, second value: '))


def tzoid_area(h, a, b):
    return ((a + b) * h)/2


print('Expected Output:', tzoid_area(h, a, b))