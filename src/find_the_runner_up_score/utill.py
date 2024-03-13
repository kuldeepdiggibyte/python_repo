import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
def findrun():
    n = int(input())
    arr = map(int, input().split())
    array = list(arr)
    array.sort(reverse=True)
    for i in range(n):
        if array[0] > array[i]:
            logging.info(array[i])
            return array[i]
            break