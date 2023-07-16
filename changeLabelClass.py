# changeLabelClass.py

import os
import re

def change_label_class(dir_path='valid/labels/'):
    # regex pattern for lines starting with integer and followed by 4 floats
    pattern = re.compile(r'^\d+ -?\d+\.\d+ -?\d+\.\d+ -?\d+\.\d+ -?\d+\.\d+')

    # store unique integer values at the start of each line
    unique_ints = set()

    # find all unique integers
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            with open(dir_path + filename, 'r') as file:
                for line in file:
                    if pattern.match(line):
                        unique_ints.add(int(line.split()[0]))

    # print the unique integers to the user
    print(f'Unique integer values found: {unique_ints}')

    # ask the user for the integer to replace, and the new value
    old_int = int(input('Enter the integer value to replace: '))
    new_int = int(input('Enter the new integer value: '))

    # replace the old integer with the new one in each file
    for filename in os.listdir(dir_path):
        if filename.endswith(".txt"):
            with open(dir_path + filename, 'r') as file:
                lines = file.readlines()
            with open(dir_path + filename, 'w') as file:
                for line in lines:
                    if pattern.match(line) and int(line.split()[0]) == old_int:
                        line = line.replace(str(old_int), str(new_int), 1)
                    file.write(line)
    print('Replacement done.')
