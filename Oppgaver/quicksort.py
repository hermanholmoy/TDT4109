
def partition(A, low, high):
    pivot = A[high]
    i = low
    for j in range(i, high):
        if A[j] < pivot:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i += i

    temp = A[i]
    A[i] = A[high]
    A[high] = temp
    return i, A


def quicksort(A, low, high):
    print(A)
    if low < high:
        p, A = partition(A, low, high)
        quicksort(A, low, p-1)
        quicksort(A, p+1, high)
        print(A)
    else:
        return A


A = [3, 2, 4, 1, 6]
quicksort(A, 0, len(A) - 1)
