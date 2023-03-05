from time import sleep
from math import sqrt
num = int(input())
time = int(input())
sleep(time/1000)

print('Square root of', num, 'after', time, 'milliseconds is', sqrt(num))