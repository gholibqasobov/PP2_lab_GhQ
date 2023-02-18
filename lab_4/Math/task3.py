import math as m
n = int(input('Input number of sides: '))
l = int(input('Input the length of a side: '))

def polygon_area(n, l):
    a = n * pow(l, 2)
    b = 4 * m.tan(m.pi/n)
    return a // b


print('The area of polygon is:', polygon_area(n, l))