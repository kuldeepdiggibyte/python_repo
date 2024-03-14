import unittest
from src.iteratables.utill import *

from src.iteratables.utill import iterables_iterators


class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = iterables_iterators()
        expected_output = 0.833333
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
4
a a c d
2
        '''

    def test2(self):
        actual_input = iterables_iterators()
        expected_output = 1.0
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
5
a a c d a
3
        '''

    def test3(self):
        actual_input = iterables_iterators()
        expected_output = 0.9
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
5
a a c d c
3
        '''

if __name__ == '__main__':
    unittest.main()
