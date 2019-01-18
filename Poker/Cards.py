import numpy as np


class Deck:
    stack = {}
    dealt = {}
    nDealt = 0
    N = 52

    def __init__(self):
        self.initialize()

    def initialize(self):
        ii = 0
        for rank in Card.Ranks.keys():
            for suit in Card.suits:
                self.stack[ii] = Card(rank, suit)
                self.stack[ii].card_string = str(self.stack[ii].Rank) + self.stack[ii].Suit + ' '
                self.dealt[ii] = False
                ii += 1

    def deal_cards(self, nCards, show):
        iv = np.random.randint(1, 52, nCards)
        cards = []
        card_string = ''
        for c in iv:
            cards.append(self.stack[c])
            self.dealt[c] = True
            card_string += self.stack[c].card_string + ' '
        if show:
            print card_string
        return cards

    def count_cards(self, show):
        for dealt in self.dealt.values():
            if dealt:
                self.nDealt += 1
        if show:
            print str(self.nDealt) + ' Cards in play'


class Card:
    Rank = 1   # Ranks {2-14}
    Suit = ''  # Suits {S D H C}
    card_string = ''  # <RANK,SUIT>
    Ranks = {1:'2',2:'3',3:'4',4:'5', 5:'5',
             6:'6',7:'7',8:'8',9:'9',10:'10',
             11:'J',12:'Q',13:'Q',14:'A'}
    suits = ['S','D','H','C']

    def __init__(self, rank, suit):
        if rank in self.Ranks.keys() and suit in self.suits:
            self.Rank = rank
            self.Suit = suit
            self.card_string = str(self.Rank) + self.Suit

    def reveal_card(self):
        return self.card_string

    def show_card(self, hand_string):
        """
        Prints this card to the console
        :return:
        """
        print self.card_string


def main():
    d = Deck()
    hand = d.deal_cards(2, True)
    d.count_cards(True)


if __name__ == '__main__':
    main()