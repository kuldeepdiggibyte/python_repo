import re
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')

email_format = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'

def fun(s):
    return re.match(email_format, s)

def filter_mail(emails):
    return list(filter(fun, emails))
def validating_email():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    logging.info(filtered_emails)
    # print(type(filtered_emails))
    return filtered_emails