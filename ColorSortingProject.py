import numpy as np
import matplotlib
from PIL import Image
from sys import getsizeof

class Pixel:
    def __init__(self, pixel):
        self.pixel = pixel


original_image = Image.open("randcol.png")

pixel_map = original_image.convert("RGB").getdata()

width, height = original_image.size
pic_size = width * height

print(list(pixel_map))