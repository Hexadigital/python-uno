'''
Deck Class
'''

from cards import Card
from random import shuffle


class Deck:

    def __init__(self):
        cards = []
        for number in range(0, 14):
            for color in range(1, 5):
                cards.append(Card(color, number))
        for number in range(1, 14):
            for color in range(1, 5):
                cards.append(Card(color, number))
        for number in range(14, 15):
            for i in range(0, 4):
                cards.append(Card(0, number))
        self._cards = cards
