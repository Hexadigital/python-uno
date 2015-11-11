'''
Plays UNO!
@author Hexadigital
'''
from random import randint, choice, shuffle
from colorama import init, Fore, Style
from termcolor import colored
from time import sleep
from string import capwords
from copy import deepcopy

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
		hand += [deepcopy(UnoDeck[cardnum])]
		# Remove the card from the deck
		UnoDeck.remove(UnoDeck[cardnum])
	# Give the player their hand
	return hand
	
def isValidCard(tobeplayed):
	global tablecard
	# colorless cards can be played any time
	if tobeplayed[0] == "Colorless":
		return True
	# If the values or colors are the same, it can be played
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
	# Check if the card is in the hand
	if tobeplayed in hand:
		# If it is, can it be played?
		if isValidCard(tobeplayed):
			return True
		else:
			print("You can't place that card on the table.\n")
			return False
	print("That card isn't in your hand.\n")
	return False
	
def getValidCards(hand):
	valids = []
	# For each card that is in the hand...
	for i in hand:
		# If the card is playable...
		if isValidCard(i):
			# Let's add it to a list of playable cards!
			valids += [i]
	return valids
	
def CheckSpecial(card):
	global reverse
	global turncounter
	# If the card is a Reverse, reverse the turn order
	if card[1] == "Reverse":
		reverse = not reverse
	# If the card is a Skip, skip the next player
	if card[1] == "Skip":
		if reverse:
			turncounter -= 1
		else:
			turncounter += 1

def P1PlayCard(p1card):
	global p1hand
	global tablecard
	if p1card in p1hand and isValidCard(p1card):
		# Remove the card from the player's hand
		p1hand.remove(p1card)
		# If the card is colorless, let's ask what color to use
		if p1card[0] == "Colorless":
			colorchoice = ""
			# Unless the player specifies a valid color, keep asking them
			while colorchoice not in ["Green", "Blue", "Yellow", "Red"]:
				colorchoice = capwords(raw_input("What color would you like to set it to? "))
			p1card[0] = colorchoice
		# Print out a message to let the player know what happened
		print("You place a " + PrettifyCards([p1card]) + " on the table.")
		print(id(p1card))
		# Check to see if the card is special or not
		CheckSpecial(p1card)
		# Update the card on the table
		tablecard = p1card
	
def P2PlayCard(p2card):
	global p2hand
	global tablecard
	if p2card in p2hand and isValidCard(p2card):
		# Remove the card from the player's hand
		p2hand.remove(p2card)
		# If the card is colorless, let's decide what color to pick
		if p2card[0] == "Colorless":
			handcolors = []
			for i in p2hand:
				# Make a list of all the colors in the CPU's hand
				handcolors += p2hand[0]
				# Remove all the Colorless colors
				while "Colorless" in handcolors:
					handcolors.remove("Colorless")
			# Set the wild card to whatever the CPU has the most of
			p2card[0] = max(handcolors, key=handcolors.count)
		# Print out a message to let the player know what happened
		print("The guy on your left placed a " + PrettifyCards([p2card]) + " on the table.")
		print(id(p2card))
		# Check to see if the card is special or not
		CheckSpecial(p2card)
		# Update the card on the table
		tablecard = p2card
	
def P3PlayCard(p3card):
	global p3hand
	global tablecard
	if p3card in p3hand and isValidCard(p3card):
		# Remove the card from the player's hand
		p3hand.remove(p3card)
		# If the card is colorless, let's decide what color to pick
		if p3card[0] == "Colorless":
			handcolors = []
			for i in p3hand:
				# Make a list of all the colors in the CPU's hand
				handcolors += p3hand[0]
				# Remove all the Colorless colors
				while "Colorless" in handcolors:
					handcolors.remove("Colorless")
			# Set the wild card to whatever the CPU has the most of
			p3card[0] = max(handcolors, key=handcolors.count)
		# Print out a message to let the player know what happened
		print("The lady across from you placed a " + PrettifyCards([p3card]) + " on the table.")
		print(id(p3card))
		# Check to see if the card is special or not
		CheckSpecial(p3card)
		# Update the card on the table
		tablecard = p3card
	
def P4PlayCard(p4card):
	global p4hand
	global tablecard
	if p4card in p4hand and isValidCard(p4card):
		# Remove the card from the player's hand
		p4hand.remove(p4card)
		# If the card is colorless, let's decide what color to pick
		if p4card[0] == "Colorless":
			handcolors = []
			for i in p4hand:
				# Make a list of all the colors in the CPU's hand
				handcolors += p4hand[0]
				# Remove all the Colorless colors
				while "Colorless" in handcolors:
					handcolors.remove("Colorless")
			# Set the wild card to whatever the CPU has the most of
			p4card[0] = max(handcolors, key=handcolors.count)
		# Print out a message to let the player know what happened
		print("The guy on your right placed a " + PrettifyCards([p4card]) + " on the table.")
		print(id(p4card))
		# Check to see if the card is special or not
		CheckSpecial(p4card)
		# Update the card on the table
		tablecard = p4card
	
def P1Turn():
	global p1hand
	sleep(3)
	# Precursor
	print("\nYou look at your hand:")
	# Print out the players hand, complete with colors
	print(PrettifyCards(p1hand))
	# If there are no playable cards in the hand...
	if getValidCards(p1hand) == []:
		# Let's draw a card!
		newcard = DrawCard()
		p1hand += [deepcopy(newcard)]
		print("You draw a " + PrettifyCards([newcard]) + " from the deck.")
		P1PlayCard(newcard)
	else:
		# Should we print out the list of playable cards?
		if easymode:
			print("You can play: " + PrettifyCards(getValidCards(p1hand)))
		# Loop until they choose a valid card (in hand, and can be played)
		while True:
			tempcard = raw_input("What card would you like to play? ").split(None, 1)
			if len(tempcard) == 2:
				# Fix the input into a proper card type
				propercard = [capwords(tempcard[0]), capwords(tempcard[1])]
				# See if they can play that card
				if TryToPlayCard(p1hand, propercard):
					break
		# They picked a valid card! Let's play it.
		P1PlayCard(propercard)
	
def P2Turn():
	global p2hand
	sleep(3)
	if getValidCards(p2hand) == []:
		# Let's draw a card!
		newcard = DrawCard()
		p2hand += [deepcopy(newcard)]
		print("The guy on your left drew a card from the deck.")
		P2PlayCard(newcard)
	else:
		# Pick a random card from the list of valid cards
		tempcard = choice(getValidCards(p2hand))
		# Let's play it
		P2PlayCard(tempcard)
	
def P3Turn():
	global p3hand
	sleep(3)
	if getValidCards(p3hand) == []:
		# Let's draw a card!
		newcard = DrawCard()
		p3hand += [deepcopy(newcard)]
		print("The lady across from you drew a card from the deck.")
		P3PlayCard(newcard)
	else:
		# Pick a random card from the list of valid cards
		tempcard = choice(getValidCards(p3hand))
		# Let's play it
		P3PlayCard(tempcard)

def P4Turn():
	global p4hand
	sleep(3) 
	if getValidCards(p4hand) == []:
		# Let's draw a card!
		newcard = DrawCard()
		p4hand += [deepcopy(newcard)]
		print("The guy on your right drew a card from the deck.")
		P4PlayCard(newcard)
	else:
		# Pick a random card from the list of valid cards
		tempcard = choice(getValidCards(p4hand))
		# Let's play it
		P4PlayCard(tempcard)

def PrettifyCards(listofcards):
	returnstring = ''
	# For every card given...
	for i in range(0, len(listofcards)):
		i -= 1
		# If the card is blue, change the color to cyan (it looks better)
		if listofcards[i][0] == "Blue":
			returnstring += (Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1], 'cyan') + Style.RESET_ALL)
		# If the card is colorless, print it out with the system's default color
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

# Load the config
execfile('config.txt')	

# Let's start the game!
init()
turncounter = 1
reverse = False
# Generate the deck
UnoDeck = GenerateDeck()
# Generate the players' hands
p1hand = GenerateHand()
p2hand = GenerateHand()
p3hand = GenerateHand()
p4hand = GenerateHand()

# A short intro
lightercolor = ["yellow", "red"]
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
# While everyone has cards, play the game
while len(p1hand) != 0 and len(p2hand) != 0 and len(p3hand) != 0 and len(p4hand) != 0:
	# Figure out whose turn it is
	if turncounter == 1:
		P1Turn()
	elif turncounter == 2:
		P2Turn()
	elif turncounter == 3:
		P3Turn()
	elif turncounter == 4:
		P4Turn()
		RandomEvent()
	# Adjust the counter to reflect the next person's turn
	if reverse == False:
		turncounter += 1
	else:
		turncounter -= 1
	# If the counter is above or below the number of players
	# then we should adjust it so that it loops back around
	if turncounter < 1:
		turncounter += 4
	elif turncounter > 4:
		turncounter -= 4