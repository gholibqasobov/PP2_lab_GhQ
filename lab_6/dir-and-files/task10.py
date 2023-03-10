import os

path = input('Enter path: ')


def check_file_access(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            if os.access(path, os.W_OK) and os.access(path, os.R_OK) and os.access(path, os.X_OK):
                return True
    return False


def remove_file():
    os.remove(path) if check_file_access(path) else print("File path doesn't exist or access is denied!")


remove_file()
