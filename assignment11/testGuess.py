import unittest

from guess import Guess
from hangman import Hangman
from word import Word

#Guess 모듈 테스트케이스
class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('q')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testCurrentStatus(self):
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('f')
        self.assertEqual(self.g1.currentStatus, '_efau_t')
        self.g1.guess('d')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.g1.guess('l')
        self.assertEqual(self.g1.currentStatus, 'default')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('x')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u x ')

    def testDisplayFinished(self):
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.g1.guess('d')
        self.g1.guess('f')
        self.g1.guess('a')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('u')
        self.g1.guess('l')
        self.g1.guess('t')
        self.assertEqual(self.g1.finished(), True)

#Hangman 모듈 테스트케이스
class TestHangman(unittest.TestCase):

    def setUp(self):
        self.g2 = Hangman()

    def tearDown(self):
        pass

    def testDisplayDecreaseLife(self):
        self.assertEqual(self.g2.remainingLives, 6)
        self.g2.decreaseLife()
        self.assertEqual(self.g2.remainingLives, 5)
        self.g2.decreaseLife()
        self.assertEqual(self.g2.remainingLives, 4)

    def testDisplayCurrentShape(self):
        self.assertEqual(self.g2.remainingLives, 6)
        self.g2.decreaseLife()
        self.g2.decreaseLife()
        self.assertEqual(self.g2.currentShape(), '''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''')

#Word 모듈 테스트케이스
class TestWord(unittest.TestCase):

    def setUp(self):
        self.g3 = Word('words.txt')

    def tearDown(self):
        pass

    def testTest(self):
        self.assertEqual(self.g3.test(), 'default')


if __name__ == '__main__':
    unittest.main()
