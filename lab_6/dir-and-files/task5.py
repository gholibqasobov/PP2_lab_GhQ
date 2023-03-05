import os
path = input('Enter path: ')

if os.path.exists(path):
    print(os.path.basename(path))
    for item in os.listdir(path):
        d = os.path.join(path, item)
        if os.path.isdir(d):
            print(item)
else:
    print("Path doesn't exist!")