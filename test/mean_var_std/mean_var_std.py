import unittest

from src.mean_var_std.utill import mean_var_std


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mean_var_std(), 1.11803398875)

    ''' 2 2 input
            1 2
            3 4
            1.11803398875 (output)'''


    def test_2(self):
        self.assertEqual(mean_var_std(), 1.224744871392)

    '''     2 4 (input)
            7 5
            8 8
            1.224744871392 (output)'''

    def test_3(self):
        self.assertEqual(mean_var_std(), 2.793842435707)

    ''' 3 6 (input)
        8 9 
        3 4
        1 4
        2.793842435707 (output)'''






if __name__ == '__main__':
    unittest.main()
