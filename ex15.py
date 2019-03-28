# import argument from sys module
from sys import argv

# arguments are script and filename
script, filename = argv

# variable txt opens filename
txt = open(filename)

print(f"Here's your file {filename}:")
# reading the ex15_sample.txt
print(txt.read())

print("Type the filename again:")
# asking the user to input the filename again
file_again = input("> ")
# opening the file again
txt_again = open(file_again)
# printing out the ex15_sample.txt again
print(txt_again.read())

