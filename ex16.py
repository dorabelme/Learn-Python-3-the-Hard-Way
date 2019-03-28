from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that,hit CTRL/C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# variable named target
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# erasing content
target.truncate()

print("Now I'm going to ask you for three lines.")

#inputting 3 lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# writing the lines in the document
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")


print("And finally we close.")
# closing the document
target.close()



