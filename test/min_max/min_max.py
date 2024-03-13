import unittest

from src.min_max.utill import min_max


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(min_max(),6)

    ''' 4 3
        6 6
        7 3 
        7 2
        1 8
        6'''

    def test_2(self):
        self.assertEqual(min_max(),8)

    '''4 6
       9 8
       3 5 
       1 4 
       5 7
       8'''

    def test_3(self):
        self.assertEqual(min_max(),6)



'''5 7 
    7 4
    8 6
    4 6
    9 4
    5 7
    6'''


if __name__ == '__main__':
    unittest.main()
