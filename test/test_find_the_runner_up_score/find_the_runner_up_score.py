import unittest
from src.find_the_runner_up_score.utill import findrun
class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(findrun(), 5)  # add assertion here
        '''
        5
2 3 6 6 5
'''
    def test_2(self):
        self.assertEqual(findrun(), 5)  # add assertion here
        '''
        5
2 3 6 5 1
'''

    def test_3(self):
        self.assertEqual(findrun(), 7)  # add assertion here
        '''
        7
2 3 6 7 1 8 
'''

if __name__ == '__main__':
    unittest.main()
