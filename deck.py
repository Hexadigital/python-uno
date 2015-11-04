'''
Deck Class
'''

from cards import Card
from random import shuffle


class Deck:

    def __init__(self):
        cards = []
        for number in range(0, 13):
            for color in range(1, 5):
                cards.append(Card(color, number))
        for number in range(1, 13):
            for color in range(1, 5):
                cards.append(Card(color, number))
        for number in range(13, 15):
            for i in range(0, 4):
                cards.append(Card(0, number))
        self._cards = cards

    def shuffle_deck(self):
        shuffle(self._cards)

    def get_deck_length(self):
        return len(self._cards)

    def get_cards(self):
        return self._cards

    def draw(self):
        return self._cards.pop()

    def return_card(self, card):
        self._cards.append(card)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print(deck.get_deck_length())
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()

    print(deck.draw())
    print(deck.draw())
