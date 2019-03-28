# function called cheese_and_crackers with 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# printing first argument
	print(f"You have {cheese_count} cheeses!")
	# printing second argument
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# giving the function numbers
cheese_and_crackers(20, 30)

# using variables from the function
print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# doing math in the function
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# combining variables with math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

