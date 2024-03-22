import calendar
import logging

import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
def calc():
    m, d, y = map(int, input().split())
    n = calendar.weekday(y, m, d)
    day = calendar.day_name[n]
    logging.info(day.upper()) #logging.info("{:.02f}".format(average_score))
    return day.upper()
