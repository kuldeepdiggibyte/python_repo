import unittest

from src.no_idea.utill import no_idea


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(no_idea(), 1)  # add assertion here

    def test_2(self):
        self.assertEqual(no_idea(), 2)

    def test_3(self):
        self.assertEqual(no_idea(), 1)





    ''' 3 2
        1 5 3
        3 1
        5 7
        1'''

    ''' 5 5
        1 2 3 4 5
        1 3 5 7 9
        2 4 6 8 10
        1'''

    ''' 4 4
        5 2 1 6 
        5 6 2 4
        2 3 6 1
        2'''


if __name__ == '__main__':
    unittest.main()
