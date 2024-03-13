import unittest

from src.calender.utill import calc


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calc(), "WEDNESDAY")# add assertion here

    '''08 05 2015
    WEDNESDAY'''

    def test_2(self):
        self.assertEqual(calc(), "SUNDAY")

    '''12 03 2000
    SUNDAY'''

    def test_3(self):
        self.assertEqual(calc(), "FRIDAY")

    '''08 05 2016
FRIDAY'''


if __name__ == '__main__':
    unittest.main()
