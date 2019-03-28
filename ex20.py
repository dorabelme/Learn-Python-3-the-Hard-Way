# importing argv from sys module
from sys import argv

# arguments
script, input_file = argv

# function names print_all with file argument
def print_all(f):
	# reading the file and printing it
	print(f.read())

# function named rewind with file argument
def rewind(f):
	# f.seek(0) moves to the start of the file
	f.seek(0)

# function with 2 arguments: line_count and file
def print_a_line(line_count, f):
	# f.readline() is reading a line from the file
	print(line_count, f.readline())

# variable equals opening the input_file 
current_file = open(input_file)

print("First let's print the whole file:\n")

# adding current_file argument to the function print_all
print_all(current_file)

print("Now let's rewinf, kind of like a tape.")

# adding current_file to the function rewind
rewind(current_file)

print("Let's print three lines:")

# current_line is 1
current_line = 1
# adding current_line count, and current_file as two arguents to 3rd function
print_a_line(current_line, current_file)

# + 1 line
current_line += 1
print_a_line(current_line, current_file)

# + 1 line
current_line += 1
print_a_line(current_line, current_file)

