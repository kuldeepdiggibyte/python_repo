import unittest
from src.Text_alignment.utill  import text_alignment


class TextAlignment(unittest.TestCase):
    def test1(self):
        self.assertEqual(text_alignment(), '''    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H     
''')

        '''5'''

    def test2(self):
        self.assertEqual(text_alignment(),''' H 
HHH
 HH      HH     
 HH      HH     
 HH      HH     
 HHHHHHHHHH 
 HH      HH     
 HH      HH     
 HH      HH     
        HHH 
         H  
''')
        '''2'''

    def test3(self):
              self.assertEqual(text_alignment(),'''H
H   H   
H   H   
HHHHH 
H   H   
H   H   
    H 
''')
'''1'''

if __name__ == "__main__":
    unittest.main()