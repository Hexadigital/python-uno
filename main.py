'''
Play UNO through a terminal - with colour support!
@author Hexadigital
'''
from random import randint, choice, shuffle
from colorama import init, Fore, Style
from termcolor import colored
from time import sleep
from string import capwords
from copy import deepcopy

colors = ["Green", "Blue", "Yellow", "Red"]
hands = []

def GenerateDeck():
	# Specify card types, wilds, and zeroes
	zeroes = [["Green", "0"], ["Blue", "0"], ["Yellow", "0"], ["Red", "0"]]
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
	
def CheckSpecial(card, handnum):
	global reverse
	global turncounter
	# If the card is a Reverse, reverse the turn order
	if card[1] == "Reverse":
		reverse = not reverse
	# If the card is a Skip, skip the next player
	if card[1] == "Skip" or card[1] == "Draw Two" or card[1] == "Draw Four":
		if reverse:
			turncounter -= 1
		else:
			turncounter += 1
	if card[1] == "Draw Two" or card[1] == "Draw Four":
		if card[1] == "Draw Two":
			cardnumbers = [1,2]
		elif card[1] == "Draw Four":
			cardnumbers = [1,2,3,4]
		if reverse:
			otherplayer = turncounter + 1
		else:
			otherplayer = turncounter - 1
		for i in cardnumbers:
			newcard = DrawCard()
			hands[otherplayer] += [deepcopy(newcard)]
			sleep(1)
			print(names[otherplayer] + " drew a card from the deck.")

def P1PlayCard(p1card):
	global tablecard
	if p1card in hands[0] and isValidCard(p1card):
		# Remove the card from the player's hand
		hands[0].remove(p1card)
		# If the card is colorless, let's ask what color to use
		if p1card[0] == "Colorless":
			colorchoice = ""
			# Unless the player specifies a valid color, keep asking them
			while colorchoice not in ["Green", "Blue", "Yellow", "Red"]:
				colorchoice = capwords(raw_input("What color would you like to set it to? "))
			p1card[0] = colorchoice
		# Print out a message to let the player know what happened
		print("You place a " + PrettifyCards([p1card]) + " on the table.")
		# Check to see if the card is special or not
		CheckSpecial(p1card, 0)
		# Update the card on the table
		tablecard = p1card
	
def CPUPlayCard(card, handnum):
	global tablecard
	if card in hands[handnum] and isValidCard(card):
		# Remove the card from the player's hand
		hands[handnum].remove(card)
		# If the card is colorless, let's decide what color to pick
		if card[0] == "Colorless":
			handcolors = []
			for i in hands[handnum]:
				# Make a list of all the colors in the CPU's hand
				handcolors += hands[handnum][0]
				# Remove all the Colorless colors
				while "Colorless" in handcolors:
					handcolors.remove("Colorless")
			# Set the wild card to whatever the CPU has the most of
			card[0] = max(handcolors, key=handcolors.count)
		# Print out a message to let the player know what happened
		print(names[handnum] + " placed a " + PrettifyCards([card]) + " on the table.")
		# Check to see if the card is special or not
		CheckSpecial(card, handnum)
		# Update the card on the table
		tablecard = card
	
def P1Turn():
	sleep(3)
	# Precursor
	print("\nYou look at your hand:")
	# Print out the players hand, complete with colors
	print(PrettifyCards(hands[0]))
	# If there are no playable cards in the hand...
	if getValidCards(hands[0]) == []:
		# Let's draw a card!
		newcard = DrawCard()
		hands[0] += [deepcopy(newcard)]
		print("You draw a " + PrettifyCards([newcard]) + " from the deck.")
		P1PlayCard(newcard)
	else:
		# Should we print out the list of playable cards?
		if easymode:
			print("You can play: " + PrettifyCards(getValidCards(hands[0])))
		# Loop until they choose a valid card (in hand, and can be played)
		while True:
			tempcard = raw_input("What card would you like to play? ").split(None, 1)
			if len(tempcard) == 2:
				# Fix the input into a proper card type
				propercard = [capwords(tempcard[0]), capwords(tempcard[1])]
				# See if they can play that card
				if TryToPlayCard(hands[0], propercard):
					break
		# They picked a valid card! Let's play it.
		P1PlayCard(propercard)
	
def CPUTurn():
	sleep(3)
	if getValidCards(hands[turncounter-1]) == []:
		# Let's draw a card!
		newcard = DrawCard()
		hands[turncounter-1] += [deepcopy(newcard)]
		print(names[turncounter-1] + " drew a card from the deck.")
		CPUPlayCard(newcard, turncounter-1)
	else:
		# Pick a random card from the list of valid cards
		tempcard = choice(getValidCards(hands[turncounter-1]))
		# Let's play it
		CPUPlayCard(tempcard, turncounter-1)

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
	
def CheckHands():
	if len(hands[0]) != 0 and len(hands[1]) != 0 and len(hands[2]) != 0 and len(hands[3]) != 0:
		return True
	else:
		return False

# Load the config
execfile('config.txt')	

# Let's start the game!
init()
turncounter = 1
reverse = False
# Generate the deck
UnoDeck = GenerateDeck()
# Generate the players' hands
hands = [GenerateHand(), GenerateHand(), GenerateHand(), GenerateHand()]

# A short intro
#PreIntro()
# Draw a random card from the deck, and place it on the table
tablecard = DrawCard()
# If the card is a wild, pick a random color
if (tablecard[0] == "Colorless"):
	tablecard[0] = choice(colors)
DealerText(PrettifyCards([tablecard]))
#PostIntro()
# While everyone has cards, play the game
while CheckHands():
	# Figure out whose turn it is
	if turncounter == 1:
		P1Turn()
	else:
		CPUTurn()
		try:
			RandomEvent()
		except:
			False
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