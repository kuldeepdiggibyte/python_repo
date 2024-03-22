import unittest

from src.collections_named_tuple.utill import named_tuple


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(named_tuple(), 78.00)  # add assertion here

    '''5
    ID         MARKS      NAME       CLASS     
    1          97         Raymond    7         
    2          50         Steven     4         
    3          91         Adrian     9         
    4          72         Stewart    5         
    5          80         Peter      6'''


    def test_2(self):
        self.assertEqual(named_tuple(), 81.00)

    '''5
    MARKS      CLASS      NAME       ID        
    92         2          Calum      1         
    82         5          Scott      2         
    94         2          Jason      3         
    55         8          Glenn      4         
    82         2          Fergus     5 '''

    def test_3(self):
        self.assertEqual(named_tuple(), 40.00)




'''5
ID         MARKS      NAME       CLASS     
1          20         Raymond    7         
2          30         Steven     4         
3          40         Adrian     9         
4          50         Stewart    5         
5          60         Peter      6'''






if __name__ == '__main__':
    unittest.main()
