def main():
    n = int(input())
    results = []

    for _ in range(n):
        m = int(input())
        array = input()
        array = list(map(int, array.split(" ")))

        l, r = 0, len(array) - 1
        c = float('inf')
        ans = 'Yes'

        while l <= r:
            if c <= min(array[l], array[r]):
                ans = 'No'
                break
            if (c >= array[l]) and (c >= array[r]):
                if (array[l] >= array[r]):
                    c = array[l]
                    l += 1
                else:
                    c = array[r]
                    r -= 1
            elif c >= array[l]:
                c = array[l]
                l += 1
            else:
                c = array[r]
                r -= 1

        results.append(ans)
        return results


# Example usage:
results = main()
for result in results:
    print(result)
