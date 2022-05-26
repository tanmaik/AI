import re


''' A variable in python can contain any word character, [A-Za-z0-9_], but can't begin with a digit. Find variable
names that begin with digits. (Even cooler if you can exclude results between " or ' marks, to ignore strings.
That doesn't have to be done using regex, though it can be.) '''

def read_file_by_line(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    lines.insert(0, '\n')
    return lines

def find_variable_names(lines):
    wrong = []
    for index, line in enumerate(lines):
        searcher = re.search(r'\d+\w*(?=\s?=.*?)', line)
        if searcher:
            wrong.append((index, searcher.group()))
    return wrong

naming_errors = find_variable_names(read_file_by_line('error_testing.py'))

for line, error in naming_errors:
    print('Your variable name is wrong on line {}: {}'.format(line, error))

def read_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text

def find_functions(file_string):
    function_names = re.findall(r'(?<=def\s)\w+', file_string)
    return function_names

function_names = find_functions(read_file('error_testing.py'))

