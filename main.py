'''
@author Hexadigital
'''
from random import randint, choice, shuffle
from colorama import init, Fore, Style
from termcolor import colored
from time import sleep

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
	
def isValidCard(tobeplayed, topcard):
	# Colorless cards can be played anytime
	if tobeplayed[0] == "Colorless":
		return True
	# If the values or colours are the same, it can be played
	if tobeplayed[0] == topcard[0] or tobeplayed[1] == topcard[1]:
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
	
def TryToPlayCard(hand, tobeplayed, topcard):
	# Fix the input into a proper card type
	actualcard = [tobeplayed[0].capitalize(), tobeplayed[1]]
	# Check if the card is in the hand
	if actualcard in hand:
		# If it is, can it be played?
		if isValidCard(actualcard, topcard):
			return True
		else:
			print("That card can't be played!\n")
			return False
	print("That card isn't in your hand!\n")
	return False
	
def getValidCards(hand, topcard):
	valids = []
	for i in hand:
		if isValidCard(i, topcard):
			valids += [i]
	return valids

def P1PlayCard(tobeplayed):
	# Fix the input into a proper card type
	card = [tobeplayed[0].capitalize(), tobeplayed[1]]
	# Remove the card from the player's hand
	p1hand.remove(card)
	# Print out a message to let the player know what happened
	print("You place the " + PrettifyCards([card]) + " on the table.")
	# Update the card on the table
	tablecard = card
	
def P1Turn():
	# Print out the players hand, complete with colours
	print(PrettifyCards(p1hand))
	if easymode:
		print("You can play: " + PrettifyCards(getValidCards(p1hand, tablecard)))
	# Loop until they choose a valid card (in hand, and can be played)
	while True:
		tempcard = raw_input("What card would you like to play?: ").split(None, 1)
		# See if they can play that card
		if TryToPlayCard(p1hand, tempcard, tablecard):
			break
	# They picked a valid card! Let's play it.
	P1PlayCard(tempcard)

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

# Load the config
execfile('config.txt')	

# Let's start the game!
init()
lightercolor = ["yellow", "red"]
# A short intro
'''print("Welcome to the world of Uno!")
print("You sit down at a table with a few other people.")
sleep(3)'''
# Generate the deck
UnoDeck = GenerateDeck()
'''print("The dealer begins to shuffle the deck.")
sleep(1)
print("\nWhile you are waiting, you examine the other players.")
sleep(5)
print("Two of them seem to be composed, but the other is a nervous wreck.")
sleep(3)
print("You watch as he " + Style.BRIGHT + colored("lights", lightercolor[randint(0,1)]) + Style.RESET_ALL + " a cigarette to calm his nerves.")
sleep(3)'''
# Generate the players' hands
p1hand = GenerateHand()
p2hand = GenerateHand()
p3hand = GenerateHand()
p4hand = GenerateHand()
'''print("\nThe dealer gives everyone their hands.")
sleep(1)
print("You pick your cards up, but don't look at them just yet.")
sleep(2)'''
# Draw a random card from the deck, and place it on the table
tablecard = DrawCard()
print("The dealer places a " + PrettifyCards([tablecard]) + " in the centre of the table.")
'''sleep(2)
print("The scent of smoke hits your nose. It's familiar, yet unwanted.")
sleep(3)
print("\nYou start. You look at your hand:")'''
while len(p1hand) != 0 and len(p2hand) != 0 and len(p3hand) != 0 and len(p4hand) != 0:
	P1Turn()