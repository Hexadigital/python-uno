'''
Hand Class
'''

from random import choice


class Hand:

    def __init__(self):
        self._hand = []

    def draw(self, game_state):
        self._hand.append(game_state.draw_card())

    def play(self, game_state):
        playable = []
        for card in self._hand:
            if card == game_state.get_top_card():
                playable.append()

        if len(playable) != 0:
            play_card = choice(playable)
            game_state.set_top_card(play_card)
            playable.remove(play_card)
        else:
            self.draw(game_state)
