'''
@author Hexadigital
'''
from random import randint
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
	
def DrawCard():
	randcard = UnoDeck[randint(0, len(UnoDeck) - 1)]
	UnoDeck.remove(randcard)
	return [randcard]

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
numplayers = 0
print("Welcome to the world of Uno!")
print("You sit down at a table with a few other people.")
sleep(3)
UnoDeck = GenerateDeck()
print("The dealer begins to shuffle the deck.")
sleep(1)
print("While you are waiting, you examine the other players.")
sleep(5)
print("Two of them seem to be composed, but the other is a nervous wreck.")
sleep(3)
print("You watch as he " + Style.BRIGHT + colored("lights", "red") + Style.RESET_ALL + " a cigarette to calm his nerves.")

