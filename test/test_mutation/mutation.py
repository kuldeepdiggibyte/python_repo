import unittest

from src.mutation.utill import mutate_string


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mutate_string("asdes", 2, 'k'),"askes" )# add assertion here

    '''string = asdes, position = 2, character(to replace) = k
    expected output = askdes'''


    def test_2(self):
        self.assertEqual(mutate_string("amit", 0, 'q'),"qmit" )

    '''string = amit, position = 0, character(to replace) = q
        expected output = qmit'''

    def test_3(self):
        self.assertEqual(mutate_string("valrngalre", 3, 'k'),"valkngalre" )

    '''string = valrngalre, position = 3, character(to replace) = k
        expected output = valkngalre '''


if __name__ == '__main__':
    unittest.main()
