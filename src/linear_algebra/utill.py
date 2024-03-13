import numpy as np

def deter():
    n = int(input())
    arr = np.array([input().split() for i in range(n)], dtype=float)
    deterval = np.linalg.det(arr)
    print(deterval.round(2))
    return deterval.round(2)
