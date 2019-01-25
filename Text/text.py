import numpy as np, fUtility


class Textual:
    Characters = {}
    code_points = {}
    verbose = False

    def __init__(self, verbosity):
        self.verbose = verbosity
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
        if self.verbose:
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

    def retrieve_word_bag(self):
        return fUtility.execute('cat '+self.english_data_path, False)


class Word:
    spelling = list()
    word = ''   # Probably a poor choice on variable name
    label = ''  # A Word's label is one of the following categories
    categories = ['verb', 'noun', 'adjective', 'pronoun', 'preposition']

    def __init__(self, word_in):
        self.word = word_in
        self.spelling = list(word_in)

    def set_label(self, category):
        if category in self.categories:
            self.label = category
