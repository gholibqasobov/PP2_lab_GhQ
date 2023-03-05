import os

path = input('Enter path: ')


def files(path):
    for item in os.listdir(path):
        d = os.path.join(path, item)
        if os.path.isfile(d):
            print(item)


files(path)
# C:\Users\qasob\OneDrive\Documents\GitHub\PP2_lab_GhQ
# C:\Users\qasob\OneDrive\Documents\GitHub\PP2_lab_GhQ\lab_6