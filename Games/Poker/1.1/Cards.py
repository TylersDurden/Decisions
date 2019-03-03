import numpy as np


class Card:
    rank = 0
    suit = ''

    RANKS = np.array([2, 3, 4, 5, 6, 7, 8,
             9, 10, "J","Q","K","A"])

    SUITS = ['S', 'C', 'D', 'H']

    def __init__(self, r, s):
        if r in list(range(2,15,1)):
            self.rank = self.RANKS[r-2]
        if s in self.SUITS:
            self.suit = s

    def show(self, verbose):
        if verbose:
            print str(self.rank)+self.suit
            return str(self.rank) + self.suit
        else:
            return str(self.rank)+self.suit


class Deck:

    data = []
    Cards = []

    def __init__(self):
        self.initialize()

    def initialize(self):
        ranks = range(2,15,1)
        suits = ['S', 'C', 'D', 'H']
        for rank in ranks:
            for suit in suits:
                self.data.append([rank, suit])
                self.Cards.append(Card(rank, suit))
        np.random.shuffle(self.Cards)

    def deal(self, n_cards, verbose):
        cards = []
        for i in range(n_cards):
            if verbose:
                c = self.Cards.pop().show(True)
            else:
                c = self.Cards.pop().show(False)
            cards.append(c)
        return cards

