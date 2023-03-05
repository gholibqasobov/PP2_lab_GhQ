import os
path = input('Enter path: ')

if os.path.exists(path):
    print(os.listdir(path))
else:
    print("Path doesn't exist!")