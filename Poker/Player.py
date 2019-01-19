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
    virtual_deck = Cards.Deck

    def __init__(self, N, verbose):
        self.DEPTH = N
        self.DEBUG = verbose
        self.virtual_deck = Cards.Deck()
        self.hand_simulator()

    def hand_simulator(self):
        classifieds = {}
        t0 = time.time()
        hands_simulated = 0
        for i in range(self.DEPTH):
            self.virtual_deck = Cards.Deck()
            while self.virtual_deck.nDealt < self.virtual_deck.N:
                pocket = self.virtual_deck.deal_cards(2,False,False)
                flop = self.virtual_deck.deal_cards(3,False,False)
                turn = self.virtual_deck.deal_cards(1,False,False)
                river = self.virtual_deck.deal_cards(1,False,False)
                hand_info = self.evaluate(pocket,flop,turn,river)
                # Just doing this for now, obviously a work in progress
                classifieds[hands_simulated] = hand_info
                hands_simulated += 1
        t1 = time.time()
        if self.DEBUG:
            print str(hands_simulated) + " Hands simulated [" +  str(t1-t0) + "s Elapsed]"
        return classifieds

    def evaluate(self, p, f, t, r):
        cards = p
        prc, psc = self.card_counts(cards)
        cards.append(f)
        frc, fsc = self.card_counts(cards)
        cards.append(t)
        trc, tsc = self.card_counts(cards)
        cards.append(r)
        rrc, rsc = self.card_counts(cards)
        counts = {'PocketRankCount': prc,
                  'PocketSuitCount': psc,
                  'FlopSuitCount': fsc,
                  'FlopRankCount': frc,
                  'RiverRankCount':rrc,
                  'RiverSuitCount':rsc}
        return counts

    def card_counts(self, cards):
        suit_count = {'H': 0, 'D': 0, 'S': 0, 'C': 0}
        rank_count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
                      8: 0, 9: 0, 10: 0, 11: 0, 12: 0,
                      13: 0, 14: 0}
        return rank_count, suit_count