import unittest
from src.validate_email.utill import *

from src.validate_email.utill import validating_email


class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = validating_email()
        expected_output = ['sachin_tendulkar23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3
lara@hackerrank.com
sachin_tendulkar23@hackerrank.com
britts_54@hackerrank.com
        '''

    def test2(self):
        actual_input = validating_email()
        expected_output = ['manvi@diggibyte.com', 'kuldeep@diggibyte.com', 'Krishna@diggibyte.com']
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3
Krishna@diggibyte.com
kuldeep@diggibyte.com
manvi@diggibyte.com
        '''

    def test3(self):
        actual_input = validating_email()
        expected_output = ['kalai@diggibyte.com', 'prathibha@diggibyte.com']
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
2
kalai@diggibyte.com
prathibha@diggibyte.com
        '''

if __name__ == '__main__':
    unittest.main()
