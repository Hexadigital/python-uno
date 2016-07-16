# Anything that isn't one of the required functions, but is used by them, should be defined up here
lightercolor = ["yellow", "red"]

# This is an example of defined names.
names = ["You", "The guy on your left", "The lady across from you", "The guy on your right"]

playercount = 4

# This is an example of a random event. There is a 7/1000 chance of an event occuring in this theme.
def RandomEvent():
	chance = randint(0, 1000)
	if chance == 1:
		print("The dealer smiles.")
	if chance == 2:
		print("You adjust your posture.")
	if chance == 3:
		print("You feel a " + Style.BRIGHT + colored("chill", 'cyan') + Style.RESET_ALL + " run up your back.")
	if chance == 4:
		print("The lady glances around nervously.")
	if chance == 5:
		print("The bartender looks away once you notice him staring.")
	if chance == 6:
		print("The man's cigarette isn't " + Style.BRIGHT + colored("burning", lightercolor[randint(0,1)]) + Style.RESET_ALL + " down.")
	if chance == 7:
		print("You hear someone call your name, but you must have been mistaken.")

# This is the text that the user will see first upon running the game.
def PreIntro():
	print("Welcome to the world of Uno!")
	print("You sit down at a table with a few other people.")
	sleep(3)
	print("The dealer begins to shuffle the deck.")
	sleep(1)
	print("\nWhile you are waiting, you examine the other players.")
	sleep(5)
	print("Two of them seem to be composed, but the other is a nervous wreck.")
	sleep(3)
	print("You watch as he " + Style.BRIGHT + colored("lights", lightercolor[randint(0,1)]) + Style.RESET_ALL + " a cigarette to calm his nerves.")
	sleep(3)
	print("\nThe dealer gives everyone their hands.")
	sleep(1)
	print("You pick your cards up, but don't look at them just yet.")
	sleep(2)

# This is the text that will be displayed when the dealer first places a card.
def DealerText(card):
	print("The dealer places a " + card + " in the centre of the table.")

# This is the text that will be displayed after the PreIntro, and after the dealer places a card.
def PostIntro():
	sleep(2)
	print("The scent of smoke hits your nose. It's familiar, yet unwanted.")
	sleep(3)

# This is the text that will be displayed when someone is on their last card.
def OneCardLeft(name):
	if name == 0:
		print(Style.BRIGHT + "You have declared Uno!" + Style.RESET_ALL)
	else:
		print(Style.BRIGHT + names[name] + " has declared Uno!" + Style.RESET_ALL)