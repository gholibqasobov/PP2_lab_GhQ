import os


def A_to_Z_file():
    for char in range(65, 91):
        open("C:/Users/qasob/OneDrive/Documents/GitHub/PP2_lab_GhQ/lab_6/a-z files/"+chr(char)+".txt", 'x')
        # os.remove("C:/Users/qasob/OneDrive/Documents/GitHub/PP2_lab_GhQ/lab_6/a-z files/"+chr(char)+".txt")


A_to_Z_file()