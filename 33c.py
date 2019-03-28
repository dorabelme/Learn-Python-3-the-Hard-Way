def number_filler(limit, increment_by):
	i = 0
	numbers = []
	while i < limit:
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + increment_by
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	return numbers

numbers = number_filler(10, 4)

print("The numbers: ")

for num in numbers:
	print(num)

	