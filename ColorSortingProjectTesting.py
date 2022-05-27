from PIL import Image
import numpy as np
import colorsys
import sys
import random


def color_insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i][0]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def color_insertion_sort_recursive(arr, n):
    # base case
    if n <= 1:
        return

    color_insertion_sort_recursive(arr, n - 1)
    last = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while (j >= 0 and arr[j][0] > last[0]):
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last
def color_merge_sort(arr): #WIP
    if len(arr) > 1:
        mid = len(arr) // 2

        L = np.array(arr[:mid])
        R = np.array(arr[mid:])

        color_merge_sort(L)
        color_merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
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


def color_bubble_sort(arr):
    for i in arr:
        for j in range(len(arr) - 1):
            if arr[j][0] > arr[j + 1][0]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp


def md_sort(md_arr, length):
    for i in range(length):
        color_merge_sort(md_arr)
    return md_arr


def hls_pixelizer(rgb_pixel):
    r, g, b = rgb_pixel
    r = r / 255
    g = g / 255
    b = b / 255
    rgb_pixel = colorsys.rgb_to_hls(r, g, b)
    return rgb_pixel


def rgb_pixelizer(hls_pixel):
    h, l, s = hls_pixel
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r = (r * 255).astype(np.uint8)
    g = (g * 255).astype(np.uint8)
    b = (b * 255).astype(np.uint8)
    return [r, g, b]


original_image = Image.open("randcol.png")
pixel_map = original_image.convert("RGB").getdata()
width, height = original_image.size
pic_size = width * height

color_array = np.array(pixel_map, dtype=float)

# color_array = np.array([(0, 255, 0), (255, 0, 0), (0, 0, 255),
# (126, 128, 0), (150, 0, 105),
# (110, 56, 89)], dtype = float)


# print("Input:")
# print(color_array)
# print()

for i in range(len(color_array)):
    color_array[i] = hls_pixelizer(color_array[i])

print("HLS: ")
# print(color_array)
# print()

for n in range(width):
    color_merge_sort(color_array[n*width:(n+1)*width])

print("Sorted: ")
# print(color_array)
# print()
for i in range(len(color_array)):
    color_array[i] = rgb_pixelizer(color_array[i])

print("Output : ")
# print(color_array)
# print()
color_array = color_array.flatten().astype(np.uint8)
color_array = color_array.reshape(width, height, 3)
#for i in range(width):
#    for j in range(width):
#            temp = color_array[j][width - i - 1]
#            color_array[j][width - i - 1] = color_array[i][j]
#            color_array[i][j] = temp

#print(color_array)
# print(np.shape(color_array))
# print()

img = Image.fromarray(color_array, 'RGB')
img.save('colorsort9.jpg')
img.show()
