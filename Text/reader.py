import urllib, sys, text, time, os
import spell_check


def pull_sherlock_ebook():
    url = 'http://gutenberg.pglaf.org/1/6/6/1661/1661.txt'
    sherlock = urllib.urlopen(url).read().decode('utf-8')
    sh_length = len(sherlock)
    return sherlock.replace('\n', ' ').split(' '), sh_length


def first_pass_read(information, title):
    english = text.English(verbosity=True)
    alphabet = text.Textual
    print 'Reading \033[1m'+title+'\033[0m [\033[32m'+str(len(information))+"\033[0m Words] "
    n_known = 0
    unknowns = 0
    for word in information:
        try:
            # TODO: Need to check for special characters in word
            if word in english.vocabulary[len(word)]:
                n_known += 1
            else:
                trimmed = ''
                for letter in list(word):
                    if letter not in alphabet.symbols:
                        trimmed += letter
                if trimmed in english.vocabulary[len(trimmed)]:
                    n_known += 1
                else:
                    unknowns += 1
        except UnicodeWarning:
            pass
        except KeyError:
            break
    print str(float(n_known)/len(information)*100) + '% of Words Understood'
    print str(float(unknowns)/len(information)*100) + '% of Words Not Understood'
    return n_known, unknowns


def main():
    if 'demo' in sys.argv:
        t0 = time.time()
        book, n_words = pull_sherlock_ebook()
        try:
            known, unknown = first_pass_read(book, "Sherlock Holmes")
        except KeyboardInterrupt:
            pass
        print '\033[1m[Finished in \033[31m'+str(time.time()-t0)+'s\033[0m]'
        print str(known) + " Words Recognized"
        print str(unknown) + " Unknown Words Read"
    else:
        t0 = time.time()
        ex_text = "This is a simple example sentence though it isn't very long"
        known, unknown = first_pass_read(ex_text.split(' '), "example")
        print str(known) + " Words Recognized"
        print str(unknown) + " Unknown Words Read"


if __name__ == '__main__':
    main()
