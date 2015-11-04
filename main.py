'''
@author Hexadigital
'''
from random import randint
from colorama import init, Fore, Style
from termcolor import colored

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
	
def PrintPretty(listofcards):
	for i in range(0, len(listofcards) - 1):
		if listofcards[i][0] == "Blue":
			print(Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1], 'cyan') + Style.RESET_ALL)
		elif listofcards[i][0] != "Colorless":
			print(Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1], listofcards[i][0].lower()) + Style.RESET_ALL)
		else:
			print(Style.BRIGHT + colored(listofcards[i][0] + " " + listofcards[i][1], 'white') + Style.RESET_ALL)
			
# Let's start the game!
init()
UnoDeck = GenerateDeck()
p1hand = GenerateHand()
PrintPretty(p1hand)
#print("Welcome to the world of Uno!")
#numplayers = int(input("How many players will be playing today? (0-10): "))
