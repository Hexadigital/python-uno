'''
@author Hexadigital
'''
from random import randint, choice, shuffle
from colorama import init, Fore, Style
from termcolor import colored
from time import sleep
from string import capwords

def GenerateDeck():
	# Specify card types, wilds, and zeroes
	zeroes = [["Green", "0"], ["Blue", "0"], ["Yellow", "0"], ["Red", "0"]]
	colors = ["Green", "Blue", "Yellow", "Red"]
	values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Draw Two", "Reverse"]
	wilds = [["Colorless", "Wild"], ["Colorless", "Draw Four"]]
	deck = []
	# Create two of each color and value combination
	for color in colors:
		for value in values:
			deck += [[color, value]]
			deck += [[color, value]]
	# Add zeroes to the deck
	deck += zeroes
	# Add four of each wild to the deck
	for i in range(0,4):
		deck += wilds
	# Shuffle the deck
	shuffle(deck)
	# Return the deck
	return deck
	
def GenerateHand():
	hand = []
	# Make a hand of 7 cards
	for i in range(0, 7):
		# Pick a random card from the deck
		cardnum = randint(0, len(UnoDeck) - 1)
		# Add the card to the hand
		hand += [UnoDeck[cardnum]]
		# Remove the card from the deck
		UnoDeck.remove(UnoDeck[cardnum])
	# Give the player their hand
	return hand
	
def isValidCard(tobeplayed):
	global tablecard
	# Colourless cards can be played any time
	if tobeplayed[0] == "Colorless":
		return True
	# If the values or colours are the same, it can be played
	if tobeplayed[0] == tablecard[0] or tobeplayed[1] == tablecard[1]:
		return True
	# The card must not be the same
	else:
		return False
	
def DrawCard():
	# Pick a random card from the deck
	randcard = UnoDeck[randint(0, len(UnoDeck) - 1)]
	# Remove that card from the deck
	UnoDeck.remove(randcard)
	# And give that card back
	return randcard
	
def TryToPlayCard(hand, tobeplayed):
	# Fix the input into a proper card type
	actualcard = [capwords(tobeplayed[0]), capwords(tobeplayed[1])]
	# Check if the card is in the hand
	if actualcard in hand:
		# If it is, can it be played?
		if isValidCard(actualcard):
			return True
		else:
			print("You can't place that card on the table.\n")
			return False
	print("That card isn't in your hand.\n")
	return False
	
def getValidCards(hand):
	valids = []
	for i in hand:
		if isValidCard(i):
			valids += [i]
	return valids

def P1PlayCard(tobeplayed):
	# Fix the input into a proper card type
	p1card = [capwords(tobeplayed[0]), capwords(tobeplayed[1])]
	# Remove the card from the player's hand
	p1hand.remove(p1card)
	# Print out a message to let the player know what happened
	print("You place a " + PrettifyCards([p1card]) + " on the table.")
	# Update the card on the table
	return p1card
	
def P2PlayCard(p2card):
	global p2hand
	if p2card in p2hand and isValidCard(p2card):
		# Remove the card from the player's hand
		p2hand.remove(p2card)
		# Print out a message to let the player know what happened
		print("The guy on your left placed a " + PrettifyCards([p2card]) + " on the table.")
		# Update the card on the table
		return p2card
	else:
		return tablecard
	
def P3PlayCard(p3card):
	global p3hand
	global tablecard
	if p3card in p3hand and isValidCard(p3card):
		# Remove the card from the player's hand
		p3hand.remove(p3card)
		# Print out a message to let the player know what happened
		print("The lady across from you placed a " + PrettifyCards([p3card]) + " on the table.")
		# Update the card on the table
		return p3card
	else:
		return tablecard
	
def P4PlayCard(p4card):
	global p4hand
	if p4card in p4hand and isValidCard(p4card):
		# Remove the card from the player's hand
		p4hand.remove(p4card)
		# Print out a message to let the player know what happened
		print("The guy on your right placed a " + PrettifyCards([p4card]) + " on the table.")
		# Update the card on the table
		return p4card
	
def P1Turn():
	global p1hand
	sleep(3)
	# Precursor
	print("\nYou look at your hand:")
	# Print out the players hand, complete with colours
	print(PrettifyCards(p1hand))
	# If there are no playable cards in the hand...
	if getValidCards(p1hand) == []:
		# Let's draw a card!
		newcard = DrawCard()
		p1hand += [newcard]
		print("You draw a " + PrettifyCards([newcard]) + " from the deck.")
		return P1PlayCard(newcard)
	else:
		if easymode:
			print("You can play: " + PrettifyCards(getValidCards(p1hand)))
		# Loop until they choose a valid card (in hand, and can be played)
		while True:
			tempcard = raw_input("What card would you like to play?: ").split(None, 1)
			# See if they can play that card
			if TryToPlayCard(p1hand, tempcard):
				break
		# They picked a valid card! Let's play it.
		return P1PlayCard(tempcard)
	
def P2Turn():
	global p2hand
	sleep(3)
	if getValidCards(p2hand) == []:
		# Let's draw a card!
		newcard = DrawCard()
		p2hand += [newcard]
		print("The guy on your left drew a card from the deck.")
		return P2PlayCard(newcard)
	else:
		# Pick a random card from the list of valid cards
		tempcard = choice(getValidCards(p2hand))
		# Let's play it
		return P2PlayCard(tempcard)
	
def P3Turn():
	global p3hand
	sleep(3)
	if getValidCards(p3hand) == []:
		# Let's draw a card!
		newcard = DrawCard()
		p3hand += [newcard]
		print("The lady across from you drew a card from the deck.")
		return P3PlayCard(newcard)
	else:
		# Pick a random card from the list of valid cards
		tempcard = choice(getValidCards(p3hand))
		# Let's play it
		return P3PlayCard(tempcard)

def P4Turn():
	global p4hand
	sleep(3) 
	if getValidCards(p4hand) == []:
		# Let's draw a card!
		newcard = DrawCard()
		p4hand += [newcard]
		print("The guy on your right drew a card from the deck.")
		return P4PlayCard(newcard)
	else:
		# Pick a random card from the list of valid cards
		tempcard = choice(getValidCards(p4hand))
		# Let's play it
		return P4PlayCard(tempcard)

def PrettifyCards(listofcards):
	returnstring = ''
	# For every card given...
	for i in range(0, len(listofcards)):
		i -= 1
		# If the card is blue, change the colour to cyan (it looks better)
		if listofcards[i][0] == "Blue":
			returnstring += (Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1], 'cyan') + Style.RESET_ALL)
		# If the card is colorless, print it out with the system's default colour
		elif listofcards[i][0] != "Colorless":
			returnstring += (Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1], listofcards[i][0].lower()) + Style.RESET_ALL)
		# Otherwise, print it as the color that it is
		else:
			returnstring += (Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1] + Style.RESET_ALL))
		# If there are multiple cards, separate them by commas and spaces
		if i != len(listofcards) - 2:
			returnstring += ", "
	# Return the list of colored cards
	return returnstring

def RandomEvent():
	chance = randint(0, 100)
	if chance == 0:
		print("The dealer smiles.")
	if chance == 1:
		print("You adjust your posture.")
	if chance == 2:
		print("You feel a " + Style.BRIGHT + colored("chill", 'cyan') + Style.RESET_ALL + " run up your back.")
	if chance == 3:
		print("The lady glances around nervously.")
	if chance == 4:
		print("The bartender looks away once you notice him staring at you.")
	if chance == 5:
		print("The man's cigarette isn't " + Style.BRIGHT + colored("burning", lightercolor[randint(0,1)]) + Style.RESET_ALL + " down.")
	if chance == 6:
		print("You hear someone call your name, but you must have been mistaken.")
		print("Nobody here knows your name.")

# Load the config
execfile('config.txt')	

# Let's start the game!
init()
lightercolor = ["yellow", "red"]
# Generate the deck
UnoDeck = GenerateDeck()
# Generate the players' hands
p1hand = GenerateHand()
p2hand = GenerateHand()
p3hand = GenerateHand()
p4hand = GenerateHand()

# A short intro
'''print("Welcome to the world of Uno!")
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
sleep(2)'''
# Draw a random card from the deck, and place it on the table
tablecard = DrawCard()
print("The dealer places a " + PrettifyCards([tablecard]) + " in the centre of the table.")
'''sleep(2)
print("The scent of smoke hits your nose. It's familiar, yet unwanted.")
sleep(3)'''
while len(p1hand) != 0 and len(p2hand) != 0 and len(p3hand) != 0 and len(p4hand) != 0:
	P1Turn()
	P2Turn()
	P3Turn()
	P4Turn()
	RandomEvent()