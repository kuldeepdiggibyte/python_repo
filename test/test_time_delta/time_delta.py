import unittest
from datetime import datetime

from src.time_delta.utill import time_delta

class TestTimeDelta(unittest.TestCase):
    def test_time_delta_positive_offset(self):
        t1 = "Fri 01 May 2015 13:54:36 -0700"
        t2 = "Fri 01 May 2015 13:54:36 +0000"
        self.assertEqual(time_delta(t1, t2), "25200")

    def test_time_delta_negative_offset(self):
        t1 = "Sat 01 May 2021 10:30:00 +0300"
        t2 = "Sat 01 May 2021 06:30:00 +0000"
        self.assertEqual(time_delta(t1, t2), "3600")

    def test_time_delta_different_date(self):
        t1 = "Mon 15 Nov 2021 18:45:00 +0500"
        t2 = "Tue 16 Nov 2021 00:30:00 +0000"
        self.assertEqual(time_delta(t1, t2), "38700")


if __name__ == '__main__':
    unittest.main()
