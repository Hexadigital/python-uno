lightercolor = ["yellow", "red"]

def RandomEvent():
	chance = randint(0, 100)
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
	
def PostIntro():
	sleep(2)
	print("The scent of smoke hits your nose. It's familiar, yet unwanted.")
	sleep(3)