import Cards, time, sys
import numpy as np

def simulate_hands(verbose, each):
    hands = {}
    deck = Cards.Deck()
    for i in range(7):
        pocket = deck.deal(2, each)
        flop = deck.deal(3, each)
        turn = deck.deal(1, each)
        river = deck.deal(1, each)
        if verbose:
            print '\033[1mHand ' + str(i) + ' \033[0m\033[1m\033[32m' +\
                   str(pocket) + '|' + str(flop) + '|' + str(turn) + '|' + str(river)+'\033[0m'
            print '\033[1m\033[31m-------------------------------------------------\033[0m'
        hands[i] = [[pocket], [flop], [turn], [river]]
    return hands


def generate_raw_poker_data_knowledge_base(depth, debug, lvl):
    poker_data = []
    for i in range(depth):
        if debug:
            data = simulate_hands(True, lvl)
        else:
            data = simulate_hands(False, lvl)
        poker_data.append(data)
    return poker_data


def simulate_50K_hands():
    N = int(7)
    T0 = time.time()
    data = {}
    for trial in range(N):
        batch = generate_raw_poker_data_knowledge_base(1000,False, False)
        data[trial] = batch
    print "50K Hands Simulated ["+str(time.time()-T0)+"s]"
    return data, float(time.time()-T0)


def analyze_hand(hand_data):
    stats = {}
    for round in range(len(hand_data)):
        pocket = hand_data[round][0].pop()
        flop = hand_data[round][1].pop()
        turn = hand_data[round][2].pop()
        river = hand_data[round][3].pop()

        p1 = pocket[0].split('')
        p2 = pocket[1].split('')

        f1 = flop[0].split('')
        f2 = flop[1].split('')
        f3 = flop[2].split('')

        t1 = turn[0].split('')
        r1 = river[0].split('')

        stats[round] = []
    return stats


def main():
    if '-train' in sys.argv:
        t0 = time.time()
        simulate_hands(True, False)
        pt1, dt1 = simulate_50K_hands()
        pt2, dt2 = simulate_50K_hands()
        pt3, dt3 = simulate_50K_hands()
        print str(len(pt1) * len(pt1.pop(0)) * 7 * 3) + " Hands Simulated [" +\
              str(time.time() - t0) + "]"

    cards = simulate_hands(True, False)
    analyze_hand(cards)

if __name__ == '__main__':
    main()
