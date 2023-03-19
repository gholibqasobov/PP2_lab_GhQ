# items = ['Mango', 'Orange', 'Apple', 'Lemon']
# 1st method
items = []
n = int(input())
for i in range(n):
    items.append(input())

#2nd method
# items = input().split()

file = open('../text_files/task7.txt', 'w')
for item in items:
    file.write(item+'\n')
file.close()

file = open('../text_files/task7.txt', 'r')
print(file.read())
file.close()

