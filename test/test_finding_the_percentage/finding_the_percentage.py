import unittest

from src.finding_the_percentage.utill import student_avg


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(student_avg(), 60.00)  # add assertion here


    ''' 2
        kuldeep 50 60 70 
        amit 34 24 65
        kuldeep'''

    def test_2(self):
        self.assertEqual(student_avg(), 30.00)

    ''' 2
        kuldeep 20 30 40 
        amit 23 38 80
        kuldeep'''

    def test_3(self):
        self.assertEqual(student_avg(), 70.00)

    '''3
    kuldeep 40 23 54
    amit    34 23 43
    krishna 60 70 80
    krishna'''


if __name__ == '__main__':
    unittest.main()
