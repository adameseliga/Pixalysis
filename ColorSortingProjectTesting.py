from PIL import Image
import numpy as np
import colorsys
import onedimension
import pixelconvert
import sys
import random


def color_bubble_sort(arr):
    for i in arr:
        for j in range(len(arr) - 1):
            if arr[j][0] > arr[j + 1][0]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp


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

pixelconvert.hls(color_array)

print("HLS: ")
# print(color_array)
# print()

onedimension.bubblesort(color_array, 0) #n*width:(n+1)*width

print("Sorted: ")
# print(color_array)
# print()
pixelconvert.rgb(color_array)

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
img.save('colorsort10.jpg')
img.show()
