import numpy as np


# Image data retrieved from PIL is represented as a 2D array that behaves like a 1D array.
# Thus, you don't have to call np.flatten() for these methods.


def mergesort(arr, v):  # Accepts image data as a list and the value that of which it is sorting.
    # Must be represented as a tuple/array of HLS parameters.

    if len(arr) > 1:
        mid = len(arr) // 2

        L = np.array(arr[:mid])
        R = np.array(arr[mid:])

        mergesort(L, v)
        mergesort(R, v)

        i = j = k = 0

        while i < len(L) and j < len(R):  # Sort the two objects by hue.
            if (L[i][v] < R[j][v]) or (L[i][v] == R[j][v]):
                arr[k] = L[i]
                i += 1
            elif L[i][v] > R[j][v]:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# VERY inefficient for 1D arrays
def insertionsort(arr, v):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = tuple(arr[i])
        j = i - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key[v] < arr[j][v]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at after the element just smaller than it.
        arr[j + 1] = list(key)


# VERY inefficient for 1D arrays
def bubblesort(arr, v):
    for i in arr:
        for j in range(len(arr) - 1):
            if arr[j][v] > arr[j + 1][v]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp


if __name__ == '__main__':
    print('1D sort test executed successfully from main')
