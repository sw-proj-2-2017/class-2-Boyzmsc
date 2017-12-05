import unittest

from hangman import Hangman

#Hangman 모듈 테스트케이스
class TestHangman(unittest.TestCase):

    def setUp(self):
        self.g2 = Hangman()

    def tearDown(self):
        pass

    def testDecreaseLife(self):
        self.assertEqual(self.g2.remainingLives, 6)
        self.g2.decreaseLife()
        self.assertEqual(self.g2.remainingLives, 5)
        self.g2.decreaseLife()
        self.assertEqual(self.g2.remainingLives, 4)

    def testCurrentShape(self):
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


if __name__ == '__main__':
    unittest.main()
