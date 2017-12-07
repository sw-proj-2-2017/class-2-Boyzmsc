import random

class Word:

    def __init__(self, filename):

        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):
        length = 4
        r = random.randrange(self.count)
        while len(self.words[r]) < length:
            r = random.randrange(self.count)
        word = self.words[r]
        return word
