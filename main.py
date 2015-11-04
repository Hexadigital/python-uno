'''
@author Hexadigital
'''
from random import randint

def GenerateDeck():
	zeroes = [["Green", "0"], ["Blue", "0"], ["Yellow", "0"], ["Red", "0"]]
	colors = ["Green", "Blue", "Yellow", "Red"]
	values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Draw Two", "Reverse"]
	wilds = [["Colorless", "Wild"], ["Colorless", "Draw Four"]]
	deck = []
	for color in colors:
		for value in values:
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
		print "The card number is " + str(cardnum) + ", the length of the deck is " + str(len(UnoDeck))
		# Add the card to the hand
		hand += [UnoDeck[cardnum]]
		# Remove the card from the deck
		UnoDeck.remove(UnoDeck[cardnum])
	# Give the player their hand
	return hand

# Let's start the game!
UnoDeck = GenerateDeck()
p1hand = GenerateHand()
print p1hand
