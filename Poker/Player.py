import Cards, time


class Player:
    Cards = []
    Chips = 0
    Name = ''

    def __init__(self, name, chips):
        self.Name = name
        self.Chips = chips

    def get_cards(self, hand):
        self.Cards = hand

    def show_hand(self):
        card_string = ''
        for card in self.Cards:
            card_string += str(card.Rank) + card.Suit + ' '
        print card_string


class CardLogic:

    HandTypes = ["High Card", "Pair", "Two Pair", "Three Kind",
                 "Flush", "Straight", "Full House", "Straight Flush",
                 "Four Kind", "Royal Flush"]
    Rankings = {}
    DEBUG = True
    DEPTH = 0

    def __init__(self, N, verbose):
        self.DEPTH = N
        self.DEBUG = verbose

    def hand_simulator(self):
        classifieds = {}
        t0 = time.time()
        hands_simulated = 0
        for i in range(self.DEPTH):
            self.virtual_deck = Cards.Deck()
            while self.virtual_deck.nDealt < self.virtual_deck.N:
                pocket = self.virtual_deck.deal_cards(2)
                flop = self.virtual_deck(3)
                turn = self.virtual_deck(1)
                river = self.virtual_deck(1)
                hands_simulated += 1
        t1 = time.time()
        if self.DEBUG:
            print str(hands_simulated) + " Hands simulated [" +  str(t1-t0) + "s Elapsed]"
        return classifieds
