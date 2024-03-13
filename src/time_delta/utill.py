from datetime import datetime


def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'

    time1 = datetime.strptime(t1, time_format)
    time2 = datetime.strptime(t2, time_format)

    delta_seconds = str(int(abs((time1 - time2).total_seconds())))
    return delta_seconds




t1 = "Fri 01 May 2015 13:54:36 -0700"
t2 = "Fri 01 May 2015 13:54:36 +0000"
result = time_delta(t1, t2)
print(result)





