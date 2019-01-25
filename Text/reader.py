import urllib, sys, text, time, os


def pull_sherlock_ebook():
    url = 'http://gutenberg.pglaf.org/1/6/6/1661/1661.txt'
    sherlock = urllib.urlopen(url).read().decode('utf-8')
    sh_length = len(sherlock)
    return sherlock, sh_length


def first_pass_read(word_bag, text, title):
    vocab_size = len(word_bag)
    print 'Reading \033[1m'+title+'\033[0m [\033[32m'+str(len(text))+"\033[0m Words] "


def main():
    if 'demo' in sys.argv:
        t0 = time.time()
        english = text.English(verbosity=True).retrieve_word_bag()
        book, n_words = pull_sherlock_ebook()
        first_pass_read(english, book, "Sherlock Holmes")
        print '\033[1m[Finished in \033[31m'+str(time.time()-t0)+'s\033[0m]'


if __name__ == '__main__':
    main()
