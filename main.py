import os
from fnmatch import fnmatch

root = '/recents'
pattern = "*.txt"
file_list = []

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            file_list += name

def check_files(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    keywords = ['password', 'login', 'username', 'secret']

    sus = False

    for line in lines:

        line = line.strip()

        words = line.split()


        for word in words:
            if word in keywords:
                sus = True
                break

    if sus:
        return 'Suspicious keyword found in file'
    else:
        return 'No suspicious words found'

