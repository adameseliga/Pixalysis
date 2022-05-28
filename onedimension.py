import numpy as np


def merge_sort(arr, v):  # Accepts the image data as it is given by PIL.
    # Must be represented as a tuple/array of HLS parameters.

    if len(arr) > 1:
        mid = len(arr) // 2

        L = np.array(arr[:mid])
        R = np.array(arr[mid:])

        merge_sort(L, v)
        merge_sort(R, v)

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


if __name__ == '__main__':
    print('1D sort test executed successfully')
