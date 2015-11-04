'''
@author Hexadigital
'''
from random import randint, choice
from colorama import init, Fore, Style
from termcolor import colored
from time import sleep

def GenerateDeck():
	zeroes = [["Green", "0"], ["Blue", "0"], ["Yellow", "0"], ["Red", "0"]]
	colors = ["Green", "Blue", "Yellow", "Red"]
	values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Draw Two", "Reverse"]
	wilds = [["Colorless", "Wild"], ["Colorless", "Draw Four"]]
	deck = []
	for color in colors:
		for value in values:
			deck += [[color, value]]
			deck += [[color, value]]
	deck += zeroes
	for i in range(0,4):
		deck += wilds
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
	if tobeplayed[0] == "Colorless":
		return True
	if tobeplayed[0] == topcard[0] or tobeplayed[1] == topcard[1]:
		return True
	else:
		return False
	
def DrawCard():
	randcard = UnoDeck[randint(0, len(UnoDeck) - 1)]
	UnoDeck.remove(randcard)
	return randcard
	
def TryToPlayCard(hand, tobeplayed, topcard):
	actualcard = [tobeplayed[0].capitalize(), tobeplayed[1]]
	if actualcard in hand:
		if isValidCard(actualcard, topcard):
			return True
		else:
			print("That card can't be played!")
			return False
	print("That card isn't in your hand!")
	return False

def P1PlayCard(tobeplayed):
	card = [tobeplayed[0].capitalize(), tobeplayed[1]]
	p1hand.remove(card)
	print("You place the " + PrettifyCards([card]) + " on the table.")
	tablecard = card

def PrettifyCards(listofcards):
	returnstring = ''
	for i in range(0, len(listofcards)):
		i -= 1
		if listofcards[i][0] == "Blue":
			returnstring += (Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1], 'cyan') + Style.RESET_ALL)
		elif listofcards[i][0] != "Colorless":
			returnstring += (Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1], listofcards[i][0].lower()) + Style.RESET_ALL)
		else:
			returnstring += (Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1] + Style.RESET_ALL))
		if i != len(listofcards) - 2:
			returnstring += ", "
	return returnstring
			
# Let's start the game!
init()
lightercolor = ["yellow", "red"]
'''print("Welcome to the world of Uno!")
print("You sit down at a table with a few other people.")
sleep(3)'''
UnoDeck = GenerateDeck()
'''print("The dealer begins to shuffle the deck.")
sleep(1)
print("\nWhile you are waiting, you examine the other players.")
sleep(5)
print("Two of them seem to be composed, but the other is a nervous wreck.")
sleep(3)
print("You watch as he " + Style.BRIGHT + colored("lights", lightercolor[randint(0,1)]) + Style.RESET_ALL + " a cigarette to calm his nerves.")
sleep(3)'''
p1hand = GenerateHand()
p2hand = GenerateHand()
p3hand = GenerateHand()
p4hand = GenerateHand()
'''print("\nThe dealer gives everyone their hands.")
sleep(1)
print("You pick your cards up, but don't look at them just yet.")
sleep(2)'''
tablecard = DrawCard()
print("The dealer places a " + PrettifyCards([tablecard]) + " in the centre of the table.")
'''sleep(2)
print("The scent of smoke hits your nose. It's familiar, yet unwanted.")
sleep(3)
print("\nYou start. You look at your hand:")'''
print(PrettifyCards(p1hand))
while True:
	tempcard = raw_input("What card would you like to play?: ").split(None, 1)
	if TryToPlayCard(p1hand, tempcard, tablecard):
		break
P1PlayCard(tempcard)
