import os

path = input('Enter path: ')


def file_and_dir(path):
    print([item for item in os.listdir(path)])


file_and_dir(path)
