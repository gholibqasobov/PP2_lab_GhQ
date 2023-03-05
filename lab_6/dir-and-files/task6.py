file = open('task6.txt', 'r')
count = 0
for line in file:
    count += 1
print(count)

file.close()