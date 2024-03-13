import calendar
def calc():
    m, d, y = map(int, input().split())
    n = calendar.weekday(y, m, d)
    day = calendar.day_name[n]
    print(day.upper())
    return day.upper()
