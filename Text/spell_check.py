import sys, text


def word_search(vocabulary, target, verbose):
    # TODO: missing words mispelled with added letters
    close_ones = []
    same_length = []
    correct = False
    for word in vocabulary:
        N = len(list(word))
        letters = list(target)
        matches = 0
        if len(letters) == N:
            lets = list(word)
            lets.reverse()
            for letter in letters:
                try:
                    if letter == lets.pop():
                        matches += 1
                except IndexError:
                    break
                correct = True
            if float(matches)/len(target) >= 0.66:
                close_ones.append(word)
            same_length.append(word)
    if verbose:
        if matches == N:
            print word + " is spelled correctly"
        print "Target '" + target + "' is " + str(len(list(target))) + ' letters'
        print "Found " + str(len(close_ones)) + " very similar words"
        for choice in close_ones:
            print '\033[1m\t[*] ' + choice + '\033[0m'
        print "Also found " + str(len(same_length)) + " other " + \
              str(len(list(target))) + ' letter words.'
    return close_ones, same_length, correct


def main():
    if '-s' in sys.argv:
        word_in = sys.argv[2]
        vocabulary = text.English(True).retrieve_word_bag()
        close,same_size,correct = word_search(vocabulary,word_in, False)
        if not correct:
            print word_in + ' is probably spelled incorrectly'
            print "Were you looking for: "
            for word in close:
                print word
    if '-debug' in sys.argv:
        word_in = sys.argv[2]
        word_search(vocabulary, word_in, True)
    if 'alt' in sys.argv:
        vocabulary = text.English(True).retrieve_word_bag()
        if sys.argv[2] in vocabulary:
            print sys.argv[2]


if __name__ == '__main__':
    main()
