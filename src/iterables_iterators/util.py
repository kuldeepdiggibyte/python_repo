from itertools import combinations
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')

def iterables_iterators():

    N = int(input())
    N_list = input().split()
    K = int(input())

    all_comb = list(combinations(N_list, K))
    length = 0
    for i in all_comb:
        if 'a' in i:
            length +=1
    probability = length / len(all_comb)
    logging.info(round(probability, 6))
    return (round(probability, 6))