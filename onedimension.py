import numpy as np
#Image data retrieved from PIL is represented as a 2D array that behaves like a 1D array.
#Thus, you don't have to call np.flatten() for these methods.


def mergesort(arr, v):  #Accepts image data as a list and the value that of which it is sorting.
    # Must be represented as a tuple/array of HLS parameters.

    if len(arr) > 1:
        mid = len(arr) // 2

        L = np.array(arr[:mid])
        R = np.array(arr[mid:])

        mergesort(L, v)
        mergesort(R, v)

        i = j = k = 0

        while i < len(L) and j < len(R): # Sort the two objects by hue.
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

def insertionsort(arr, v):
    pass

if __name__ == '__main__':
    print('1D sort test executed successfully from main')
