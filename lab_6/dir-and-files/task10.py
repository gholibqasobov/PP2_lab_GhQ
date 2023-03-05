import os

path = input('Enter path: ')


def check_file_access(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            if os.access(path, os.W_OK) and os.access(path, os.R_OK) and os.access(path, os.X_OK):
                os.remove(path)


check_file_access(path)