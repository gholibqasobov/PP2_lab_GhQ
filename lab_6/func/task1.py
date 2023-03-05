from functools import reduce
li = [1, 2, 3, 4, 5, 6]

result = reduce(lambda x, y: x * y, li)

print(result)

