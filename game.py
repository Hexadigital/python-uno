'''
Game State Class
'''

from deck import Deck
from hand import Hand


class Game:

    def __init__(self, number_players=2, deck=Deck()):
        self._players = []
        for i in range(0, number_players):
            self._players.append(Hand())

        self._deck = deck.shuffle()
        self._top_card = deck.draw()
        self._current_player = 0

    def deal_players(self):
        for i in range(0, 7):
            for player in self._players:
                player.draw(self)

    def draw_card(self):
        return self._deck.draw()

    def get_top_card(self):
        return self._top_card

    def set_top_card(self, card):
        if self._top_card == card:
            self._top_card = card
            return True
        else:
            return False
