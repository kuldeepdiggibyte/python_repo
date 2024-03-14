import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')
def print_values(new_str):
    p = ""
    for i in new_str:
        if i not in p:
            p = p + i
    # logging.info(p)
    return p


def merge_the_tools():
    # your code goes here
    str1=""
    string, k = input(), int(input())
    parts = [string[i:i + k] for i in range(0, len(string), k)]
    for new_str in parts:
        str1+= (print_values(new_str)+"\n")
    logging.info(str1)
    return str1