import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')

def print_formatted(number):
    width = len(f"{number:b}")
    for i in range(1,number+1):
        logging.info(f"{i:>{width}} {i:>{width}o} {i:>{width}X} {i:>{width}b}")




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)