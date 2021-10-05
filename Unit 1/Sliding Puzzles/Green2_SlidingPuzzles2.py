import sys

def use_file(filename):
    with open(filename) as f:
        line_list = ["4 " + line.strip() for line in f]
    return line_list
