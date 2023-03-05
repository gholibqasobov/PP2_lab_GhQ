import os
path = input('Enter path: ')


# def dir_only(path):
#     return [item for item in os.listdir(path) if '.' not in item]


def dir_only(path):
    for file in os.listdir(path):
        d = os.path.join(path, file)
        if os.path.isdir(d):
            print(file)


dir_only(path)


# C:\Users\qasob\OneDrive\Documents\GitHub\PP2_lab_GhQ\lab_6