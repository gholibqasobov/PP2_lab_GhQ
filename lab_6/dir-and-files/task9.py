import shutil

# 1st method
with open('../text_files/task7.txt', 'r') as firstfile, open('../text_files/task9.txt', 'w') as secondfile:
    for line in firstfile:
        secondfile.write(line)


# 2nd method
shutil.copyfile('../text_files/task7.txt', '../text_files/task9.txt')