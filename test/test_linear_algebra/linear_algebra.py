import unittest

from src.linear_algebra.utill import deter

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(deter(), 5.22)

    '''2
    3.4 1.2
    6.7 3.9
    5.22'''

    def test_2(self):
        self.assertEqual(deter(), 27.52)

    '''2
    5.6 3.2
    1.2 5.6
    27.52'''

    def test_3(self):
        self.assertEqual(deter(), 4.84)

    '''2
    3.4 1.2
    5.6 3.4
    4.84'''

if __name__ == '__main__':
    unittest.main()
