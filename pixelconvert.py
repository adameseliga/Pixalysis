import numpy as np
import colorsys


def hls(arr):
    def rgb_driver(pixel):
        r, g, b = pixel
        r = r / 255
        g = g / 255
        b = b / 255
        pixel = colorsys.rgb_to_hls(r, g, b)
        return pixel
    for num in range(len(arr)):
        arr[num] = rgb_driver(arr[num])


def rgb(arr):
    def hls_driver(pixel):
        h, l, s = pixel
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        r = (r * 255).astype(np.uint8)
        g = (g * 255).astype(np.uint8)
        b = (b * 255).astype(np.uint8)
        return [r, g, b]
    for num in range(len(arr)):
        arr[num] = hls_driver(arr[num])
