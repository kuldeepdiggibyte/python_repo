import unittest

from src.word_order.utill import fun


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fun(),"2 1 1" )  # add assertion here

    def test_2(self):
        self.assertEqual(fun(),"2 1 1" )

    def test_3(self):
        self.assertEqual(fun(),"3 1 1" )

    '''4
        asdfg
        asdfg
        ertw
        vfsxs
        2 1 1 
        '''


    ''' 4
        bcdef
        abcdefg
        bcde
        bcdef
        3
        2 1 1 '''


if __name__ == '__main__':
    unittest.main()
