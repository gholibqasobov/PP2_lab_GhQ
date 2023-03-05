import os

# rootdir = input()
# for file in os.listdir(rootdir):
#     d = os.path.join(rootdir, file)
#     if os.path.isdir(d):
#         print(d)

path = input('Enter path: ')


def file_and_dir(path):
    print([item for item in os.listdir(path)])


file_and_dir(path)