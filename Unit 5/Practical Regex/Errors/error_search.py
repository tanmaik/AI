import re
import sys

file_name = sys.argv[1]

''' Error 1: Find invalid variable names. '''

print("Error 1:")

def read_file_by_line(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    lines.insert(0, '\n')
    return lines

def find_incorrect_variable_names(lines):
    wrong = []
    for index, line in enumerate(lines):
        searcher = re.search(r'\d+\w*(?=\s?=.*?)', line)
        if searcher:
            wrong.append((index, searcher.group()))
    return wrong

naming_errors = find_incorrect_variable_names(read_file_by_line(file_name))

for line, error in naming_errors:
    print('\tYour variable name is wrong on line {}: {}'.format(line, error))

''' Error 2: Find function calls to variable names. '''

def read_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text

def find_variable_names(file_string):  
    variable_names = re.findall(r'\w+(?=\s?=\s?\w+)', file_string)
    return variable_names

variable_names = find_variable_names(read_file(file_name))

def find_variable_function_calls(lines):
    function_calls = []
    for index, line in enumerate(lines): 
        searcher = re.findall(r'\w+(?=\()', line)
        for searched in searcher:
            if searched in variable_names:
                function_calls.append((index, searched))
    return function_calls

variable_function_calls = find_variable_function_calls(read_file_by_line(file_name))

print("Error 2:")
for wrong in variable_function_calls:
    print('\tYour function call is being made to a variable on line {}: {}'.format(wrong[0], wrong[1]))

''' Error 3: Find erroneous = instead of ==. '''
def find_wrong_equals(lines):
    wrong = []
    for index, line in enumerate(lines):
        searcher = re.search(r'if\s?[A-Za-z0-9 %*()]*[=]\s?[A-Za-z0-9]*?:', line)
        if searcher:
            wrong.append((index, searcher.group()))
    return wrong

print("Error 3:")
for wrong in find_wrong_equals(read_file_by_line(file_name)):
    print('\tYour if statement is using the wrong equals sign on line {}: {}'.format(wrong[0], wrong[1]))

''' Error 4: Find erroneous == instead of = . '''
def find_wrong_other_equals(lines):
    wrong = []
    for index, line in enumerate(lines):
        searcher = re.search(r'^\w+\d*\s?==\s?', line)
        if searcher:
            wrong.append(index)
    return wrong

print("Error 4: ")
for wrong in find_wrong_other_equals(read_file_by_line(file_name)):
    print('\tYour equals sign should be = on line {}.'.format(wrong))

''' Error 5: Find missing colons in Python. '''
def find_if_statements(lines):
    wrong = []
    for index, line in enumerate(lines):
        searcher = re.search(r'if [A-Za-z0-9 !@#$%^&*()]*$', line)
        if searcher:
            wrong.append((index, searcher.group()))
        searcher = re.search(r'for [A-Za-z0-9 !@#$%^&*()]*$', line)
        if searcher:
            wrong.append((index, searcher.group()))
        searcher = re.search(r'while [A-Za-z0-9 !@#$%^&*()]*$', line)
        if searcher:
            wrong.append((index, searcher.group()))
        searcher = re.search(r'def [A-Za-z0-9 !@#$%^&*()]*$', line)
        if searcher:
            wrong.append((index, searcher.group()))
    return wrong

print("Error 5: ")
for wrong in find_if_statements(read_file_by_line(file_name)):
    print('\tYour statement is missing a colon on line {}.'.format(wrong[0]))
