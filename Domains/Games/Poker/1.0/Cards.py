import numpy as np
import Player


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

    def deal_cards(self, nCards, show, verbose):
        iv = np.random.randint(1, 52, nCards)
        cards = []
        card_string = ''
        for c in iv:
            if not self.dealt[c]:
                cards.append(self.stack[c])
                self.dealt[c] = True
                card_string += self.stack[c].card_string + ' '
            else:
                c = np.random.randint(1,52,nCards)[0]
                cards.append(self.stack[c])
                self.dealt[c] = True
                card_string += self.stack[c].card_string + ' '
        if show:
            print card_string
        if verbose:
            self.count_cards(True)
        return cards

    def count_cards(self, show):
        for dealt in self.dealt.values():
            if dealt:
                self.nDealt += 1
        if show:
            print str(self.nDealt) + ' Cards in play'
        return self.nDealt


class Card:
    Ranks = {1: '2', 2: '3', 3: '4', 4: '5', 5: '5',
             6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
             11: 'J', 12: 'Q', 13: 'Q', 14: 'A'}
    Rank = 1   # Ranks {2-14}
    Suit = ''  # Suits {S D H C}
    card_string = ''  # <RANK,SUIT>
    suits = ['S','D','H','C']

    def __init__(self, rank, suit):
        if rank in self.Ranks.keys() and suit in self.suits:
            self.Rank = rank
            self.Suit = suit
            self.card_string = str(self.Rank) + self.Suit

    def reveal_card(self):
        return self.card_string

    def show_card(self):
        """
        Prints this card to the console
        :return:
        """
        print self.card_string


def main():
    # player_one = Player.Player('Player1', 1000)
    # d = Deck()
    #
    # hand = d.deal_cards(5, False, True)
    # d.count_cards(False)
    # player_one.get_cards(hand)
    # player_one.show_hand()
    stats_10_Deck = Player.CardLogic(10, True)
    stats_100_Deck = Player.CardLogic(100, True)
    stats_1K_Decks = Player.CardLogic(1000, True)
    stats_10K_Decks = Player.CardLogic(10000, True)






if __name__ == '__main__':
    main()