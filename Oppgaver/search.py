def binary_search(l, n):
    l1, l2 = l[: int(len(l) / 2)], l[int(len(l) / 2) :]
    print(l1, l2)
    if l1[-1] > n:
        # n er i l1
        return 1 + binary_search(l1, n)
    elif l2[0] < n:
        # n er i l2
        return 1 + binary_search(l2, n)


l = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(l, 4))