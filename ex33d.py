def number_filler(limit, increment_by):
	numbers = []
	for i in range(0, limit, increment_by):
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + increment_by
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	return numbers

numbers = number_filler(10, 2)

print("The numbers: ")

for num in numbers:
	print(num)
