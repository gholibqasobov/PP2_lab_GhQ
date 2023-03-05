items = ['Mango', 'Orange', 'Apple', 'Lemon']

file = open('../text_files/task7.txt', 'w')
for item in items:
    file.write(item+'\n')
file.close()

file = open('../text_files/task7.txt', 'r')
print(file.read())
file.close()

