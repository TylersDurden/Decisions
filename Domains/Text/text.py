import numpy as np, fUtility


class Textual:
    Characters = {}
    code_points = {}
    verbose = False

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
                    '(', ')', '-', '_', '=', '+', '{', '[',
                    ']', '}', "'", '"', ';', ':', '/', '?',
                    '.', ',', '>', '<', '|', '\\']

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z']
    Alphas = []

    def __init__(self, verbosity):
        self.verbose = verbosity
        self.initialize()

    def initialize(self):
        # Define possible characters
        for let in self.letters:
            self.Alphas.append(let.upper())
        # Making a bag of characters
        ii = 0
        for l in self.letters:
            self.Characters[ii] = l
            ii += 1
        for L in self.Alphas:
            self.Characters[ii] = L
            ii += 1
        for s in self.symbols:
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
    vocabulary = {}

    def __init__(self, verbosity):
        self.verbose = verbosity
        self.initialize()

    def initialize(self):
        # Need a Bag of Words
        # (* linux: /usr/share/dict *)
        english_data = fUtility.execute('cat '+self.english_data_path, False)
        if self.verbose:
            print str(len(english_data)) + ' English words in Vocabulary'
        self.vocab_size = len(english_data)
        # Create dictionary with word length as keys
        self.sort_words(english_data)

    def sort_words(self, word_data):
        longest_word = 0
        for word in word_data:
            if len(list(word)) > longest_word:
                longest_word = len(word)
        keys = np.arange(0, 50, 1)
        for word_length in keys:
            self.vocabulary[word_length] = list()
        for element in word_data:
            self.vocabulary[len(list(element))].append(element)

    def retrieve_word_bag(self):
        return fUtility.execute('cat '+self.english_data_path, False)


class Word:
    spelling = list()
    word = ''   # Probably a poor choice on variable name
    label = ''  # A Word's label is one of the following categories
    categories = ['verb', 'noun', 'adjective', 'pronoun', 'preposition']
    synonyms = []

    def __init__(self, word_in):
        self.word = word_in
        self.spelling = list(word_in)

    def set_label(self, category):
        if category in self.categories:
            self.label = category

