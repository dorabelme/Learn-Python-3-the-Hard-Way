i = 0
chosen_numbers = i < 6

def numbers(i):
	print(f"At the top i is {i}")
	print(f"Numbers now: [{i}]")
	print(f"At the bottom i is {i + 1}")


chosen_numbers = numbers(0)
chosen_numbers = numbers(1)
chosen_numbers = numbers(2)
chosen_numbers = numbers(3)
chosen_numbers = numbers(4)
chosen_numbers = numbers(5)
chosen_numbers = numbers(6)

print("The numbers: ")
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
	print(num)
