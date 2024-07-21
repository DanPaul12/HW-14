import os

def list_directory_contents(path):
    dir_list = os.listdir(path)
    print(dir_list)

list_directory_contents("/")