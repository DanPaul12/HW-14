import os

def list_directory_contents(path):
    try:
        dir_list = os.listdir(path)
        print(dir_list)
    except FileNotFoundError:
        print("That ain't a file or directory")

list_directory_contents("/")