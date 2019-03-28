from sys import exit

# function defining entrepreneur_room inside entrepreneurship_room
def entrepreneur_room():
	print("You completed your first challenge!")
	print("Let's move on! Are you an entrepreneur?")
	print("This room is full of free money. How much do you take?")
	choice = input("> ")

	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn how to type!")

	if how_much < 1000000:
		print("That's not gonna be enough for starting a company! You lost!")
		exit(0)
	if how_much > 1000000:
		print("Nice, you are a real entrepreneur! You won!")
		exit(0)

# function defining entrepreneurship_room to the left
def entrepreneurship_room():
	print("What do you think entrepreneurs need in business?")
	print("Name 3 skills! If you get one right, you can proceed.")
	empty_string = False

	while True:
		skills = input("> ")

		if "problem solving" in skills:
			print("You got it right! Gathered 5 points!")
			print("Wanna continue? Type open door...")
		elif "hard work" in skills:
			print("Yasss! Gathered 5 points!")
			print("Wanna continue? Type open door...")
		elif "execution" in skills:
			print("You got it right! Gathered 5 points!")
			print("Wanna continue? Type open door...")
		elif "risk taking" in skills:
			print("Here you go! Gathered 5 points!")
			print("Wanna continue? Type open door...")
			empty_string = True
		elif "open door" in skills:
			print("You can proceed to the next level!")
			entrepreneur_room()
		else:
			print("I don't know what you mean!")

# function defining promotion_room 
def promotion_room():	
	print("You completed your first challenge!")
	print("Let's move on! Your boss promotes you.")
	print("You have two choices: Accept it or Quit and Follow your Dreams.")
	print("Which one do you pick? 1 or 2?")
	choice = input("> ")

	if choice == "1":
		print("Congrats! You won $1,000,000!")
		exit(0)
	elif choice == "2":
		entrepreneur_room()
	else:
		print("I don't understand what you mean...")

# function defining employee_room to the right
def employee_room():
	print("Which skills do employees need at work?")
	print("Name 3 skills! If you get one right, you can proceed.")
	empty_string = False

	while True:
		skills = input("> ")

		if "life long learning" in skills:
			print("You got it right! Gathered 5 points!")
			print("Wanna continue? Type open door...")
		elif "communication" in skills:
			print("Yasss! Gathered 5 points!")
			print("Wanna continue? Type open door...")
		elif "decision making" in skills:
			print("You got it right! Gathered 5 points!")
			print("Wanna continue? Type open door...")
		elif "innovation" in skills:
			print("Here you go! Gathered 5 points!")
			print("Wanna continue? Type open door...")
			empty_string = True
		elif "open door" in skills:
			print("You can proceed to the next level!")
			promotion_room()
		else:
			print("I don't know what you mean!")

def dead(why):
	print(why, "Good job!")
	exit(0)

# function defining the start of the game
print("Welcome to the House Game!")
print("Every room hides a puzzle that will give you points if you solve them!")
print("You can start by going left or right...")

choice = input("> ")

if choice == "left":
	 entrepreneurship_room()

elif choice == "right":
	employee_room()

else:
	dead("I don't understand what you're typing.")

start()