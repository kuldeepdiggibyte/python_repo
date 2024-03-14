import unittest

from src.pilling_up.utill import main

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main(), ['No'])  # add assertion here



'''2
6
4 3 2 1 3 4'''

'''2
6
9 3 4 1 3 1'''


if __name__ == '__main__':
    unittest.main()
