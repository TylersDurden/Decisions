import numpy as np, fUtility


class Textual:
    Characters = {}
    code_points = {}

    def __init__(self):
        self.initialize()

    def initialize(self):
        # Define possible characters
        Alphas = []
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                   'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z']
        for let in letters:
            Alphas.append(let.upper())
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
                   '(', ')', '-', '_', '=', '+', '{', '[',
                   ']', '}', "'", '"', ';', ':', '/', '?',
                   '.', ',', '>', '<', '|', '\\']

        # Making a bag of characters
        ii = 0
        for l in letters:
            self.Characters[ii] = l
            ii += 1
        for L in Alphas:
            self.Characters[ii] = L
            ii += 1
        for s in symbols:
            self.Characters[ii] = s
            ii += 1
        for symbol in self.Characters.values():
            self.code_points[symbol] = ord(symbol)
        print "Mapped Codepoints " + str(np.array(self.code_points.values()).min()) + \
              '-' + str(np.array(self.code_points.values()).max())


class English:
    english_data_path = '/usr/share/dict/american-english'
    vocab_size = 0
    verbose = False

    def __init__(self, verbosity):
        self.verbose = verbosity
        self.initialize()

    def initialize(self):
        # Need a Bag of Words
        # (* linux: /usr/share/dict *)
        english_data = fUtility.execute('cat '+self.english_data_path, False)
        if self.verbose:
            print str(len(english_data)) + ' English words found'
        self.vocab_size = len(english_data)

    def retrieve_wordlist(self):
        return fUtility.execute('cat '+self.english_data_path, False)
