from collections import Counter


def fun():
    n = int(input("Enter the number of elements: "))
    l = []

    for i in range(n):
        l.append(input(f"Enter element {i + 1}: "))

    c = Counter(l)
    return ' '.join(str(value) for value in c.values())


# Example usage:
counts_string = fun()
print("Counts:", counts_string)
