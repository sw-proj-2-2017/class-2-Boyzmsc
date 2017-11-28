from hangman import Hangman
from guess import Guess
from word import Word
import re

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:


        display = hangman.get(maxTries - guess.numTries)
        print(display)
        result = guess.display()
        print(result)

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue
        if re.search('[^a-z]', guessedChar):
            print('You must select a correct letter!')
            continue


        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('word [' + guess.secretWord() + ']')
        print('Success')
    else:
        print(hangman.get(0))
    
        print('word [' + guess.secretWord() + ']')
        print('guess [' + guess.currentStatus() + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
