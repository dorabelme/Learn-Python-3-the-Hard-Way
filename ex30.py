people = 30
cars = 40
trucks = 15

# if statement compares cars and people, >, <, = case
if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

# if statement compares trucks and cars, >, <, = case
if trucks > cars:
	print("That's too many trucks.")
elif trucks < cars:
	print("Maybe we could take the trucks.")
else:
	print("We still can't decide.")

# if statement compares people and trucks, > case and else
if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")

