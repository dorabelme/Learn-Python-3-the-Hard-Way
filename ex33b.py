def number_filler(limit):
	i = 0
	numbers = []
	while i < limit:
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + 1
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	return numbers

numbers = number_filler(10)

print("The numbers: ")

for num in numbers:
	print(num)

	