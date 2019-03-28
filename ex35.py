# importing exit from sys module
from sys import exit

# function defining the gold room within bear room
def gold_room():
	# intro statement
	print("This room is full of gold. How much do you take?")
	# asking for input from player
	choice = input("> ")
	# there has to be 0 or 1 in number typed
	if "0" in choice or "1" in choice:
		# variable that turns string number to integer
		how_much = int(choice)
	# if there is no 0 or 1 in number, it prints the statement
	else:
		dead("Man, learn to type a number.")
	# if number typed is less than 50
	if how_much < 50:
		# prints statement
		print("Nice, you're not greedy, you win!")
		# exit the game
		exit(0)
	# if number is bigger than 50, printing statement
	else:
		dead("You greedy bastard!")

# function defining bear room to the left
def bear_room():
	# intro statements
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	# before a while loop, state what is False
	bear_moved = False

	# while loop
	while True:
		# choice asking for input from player
		choice = input("> ")

		# if player types take honey
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		# if player types taunt bear and does not say move the bear
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
		#loop repeats
		# statement changes to True
			bear_moved = True
		# if player types taunt bear and move bear
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		# next step to open the door
		elif choice == "open door" and bear_moved:
			# entering gold room
			gold_room()
		# anything else typed in is wrong
		else:
			print("I got no idea what that means.")

# function defining cthulhu room to the right
def cthulhu_room():
	# intro statements
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	# asking for input
	choice = input("> ")

	# if there is flee in typed text, start the game
	if "flee" in choice:
		start()
	# if there is head in typed text, you are dead
	elif "head" in choice:
		dead("Well that was tasty!")
	# any other typo, same room
	else:
		cthulhu_room()

# function, what is dead
def dead(why):
	print(why, "Good job!")
	exit(0)

# function defining start of game
def start():
	# intro statements
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	# asking for choice from player
	choice = input("> ")

	# going left or right
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	# if you type anything else, you are dead
	else:
		dead("You stumble around the room until you starve.")

# run start function 
start()

