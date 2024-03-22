import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')

def no_idea():
    input()
    read = 0
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    for i in arr:
        if i in A:
            read += 1
        elif i in B:
            read -= 1
    logging.info(read) #logging.info("{:.02f}".format(average_score))
    return read

