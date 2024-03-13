
import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    ste = "".join(l)
    logging.info(ste) #logging.info("{:.02f}".format(average_score))

    return ste

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


