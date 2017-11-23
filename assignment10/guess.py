class Guess:

    def __init__(self, word):
        self.word = word
        self.numTries = 0
        self.guessedChars = []
        self.current_Status = '_'*len(self.word)

    def display(self):
        display = 'Current: %s\nTries: %d'%(self.current_Status,self.numTries) \
                  + '\n------------------------------'
        return display

    def guess(self, character):
        if character.isalpha():
            if character in self.word:
                self.guessedChars.append(character)
                for i in range(len(self.word)):
                    if self.word[i] == character:
                        currentStatus_list = list(self.current_Status)
                        currentStatus_list[i] = character
                        self.current_Status = ''.join(currentStatus_list)
            else:
                if character in self.guessedChars:
                    pass
                else:
                    self.numTries += 1
                    self.guessedChars.append(character)


        if self.current_Status.find('_') == -1:
            return True

    def secretWord(self):
        return self.word


    def currentStatus(self):
        return self.current_Status

