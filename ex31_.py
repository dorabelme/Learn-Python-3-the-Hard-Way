print("""You have to make the biggest decision of your life.
Which one do you choose?""")
print("#1 struggling as an artist, #2 becoming a programmer")

choice = input("> ")

if choice == "1":
	print("You're gonna be broke for the rest of your life.")
	print("What will you do about it?")
	print("1. Sell your art for money and slowly start hating it.")
	print("2. You're broke but at least happy. (and lonely af)")

	artist = input("> ")

	if artist == "1":
		print("You officially became a commercial artist.")
	elif artist == "2":
		print("You spend your days as a 40 years old")
		print("dancer jealous of young teenagers. Congrats!")
	else:
		print("Probably that's a better idea!")

elif choice == "2":
	print("You're gonna turn into a nerd that you always were.")
	print("What will you do about it?")
	print("1. Accept your smarty ass and move on. At least you have tons of money!")
	print("""2. Use your beauty and intelligence, and prove you can be pretty and
	smart at the same time. No shame life! Yeah!""")

	programmer = input("> ")

	if programmer == "1":
		print("CONGRATULATIONS! You made it, bawse!")
	elif programmer == "2":
		print("Hell ya. No shame life is the best! Be a badass!")
	else:
		print("There is no other way...")

else:
	print("You think you have any other choice?")


