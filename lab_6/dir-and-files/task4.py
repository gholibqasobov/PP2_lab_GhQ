import os

path = input('Enter path: ')


def has_access(path):
    msg = ''
    if os.path.exists(path):
        if not os.access(path, os.R_OK):
            msg = 'Reading access denied!'
        elif not os.access(path, os.W_OK):
            msg = 'Writing access denied!'
        elif not os.access(path, os.X_OK):
            msg = 'Execution access denied!'
        else:
            msg = 'Access permitted!'
    else:
        msg = "File doesn't exist!"
    return msg


print(has_access(path))
# C:\Users\qasob\OneDrive\Documents\GitHub\PP2_lab_GhQ/hello world
# C:\Users\qasob\OneDrive\Documents\GitHub\PP2_lab_GhQ