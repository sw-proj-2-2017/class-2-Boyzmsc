import unittest

from word import Word

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
