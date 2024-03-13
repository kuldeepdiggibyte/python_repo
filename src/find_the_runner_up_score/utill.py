def findrun():
    n = int(input())
    arr = map(int, input().split())
    array = list(arr)
    array.sort(reverse=True)
    for i in range(n):
        if array[0] > array[i]:
            print(array[i])
            break