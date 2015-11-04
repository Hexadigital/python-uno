'''
Card Class.
'''

# 0-9, skip, reverse, draw 2 in colors
# draw 4, pick color, colorless


class Card:

    card_names = ['0',
                  '1',
                  '2',
                  '3',
                  '4',
                  '5',
                  '6',
                  '7',
                  '8',
                  '9',
                  'skip',
                  'reverse',
                  'draw 2',
                  'draw 4',
                  'pick color']

    card_colors = ['wild',
                   'red',
                   'yellow',
                   'green',
                   'blue']

    def __init__(self, color, number):
        self._color = color
        self._number = number

    def get_color(self):
        return self._color

    def get_number(self):
        return self._number

    def __eq__(self, other):
        if other.get_color == 0:
            return True
