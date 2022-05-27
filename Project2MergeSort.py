import numpy as np

def merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2

        L = a[:mid]
        R = a[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    thing = [[16], [2], [79], [4], [23], [6], [32], [3]]

    print(thing)
    merge_sort(thing)
    print(thing)

    y = np.array([(1,2,3), (4,5,6)], dtype = float)
    print(y[1][0])
