import re


''' Error 1: Find invalid variable names. '''

print("Error 1:")

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

''' Error 2: Find function calls to variable names. '''

def read_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text

def find_functions(file_string):
    function_names = re.findall(r'', file_string)
    return function_names

function_names = find_functions(read_file('error_testing.py'))

print(function_names)

def find_function_calls(file_string):
    function_calls = re.findall(r'\w+\(', file_string)
    return function_calls

function_calls = find_function_calls(read_file('error_testing.py'))

print(function_calls)
