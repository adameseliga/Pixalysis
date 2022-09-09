import os
from flask import Flask, render_template, redirect, request, flash, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import colorsys
import numpy as np

UPLOAD_FOLDER = "upload"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


def hls(arr):
    # Inputs: array of RGB pixel data
    # Outputs: array of HLS pixel data
    def rgb_driver(pixel):
        r, g, b = pixel
        r = r / 255
        g = g / 255
        b = b / 255
        H, L, S = colorsys.rgb_to_hls(r, g, b)
        return H, L, S

    for num in range(len(arr)):
        arr[num] = rgb_driver(arr[num])


def rgb(arr):
    # Inputs: array of HLS pixel data
    # Outputs: array of RGB pixel data
    def hls_driver(pixel):
        h, l, s = pixel
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        r = int((r * 255))
        g = int((g * 255))
        b = int((b * 255))
        return [r, g, b]

    for num in range(len(arr)):
        arr[num] = hls_driver(arr[num])


## Source: https://www.geeksforgeeks.org/iterative-quick-sort/
def partition(arr, l, h, value):
    i = (l - 1)
    pivot = arr[h][value]

    for j in range(l, h):
        if arr[j][value] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


## Source: https://www.geeksforgeeks.org/iterative-quick-sort/
def quickSort(arr, l, h, value):
    size = h - l + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, h, value)

        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def image_sort(filepath, UPLOAD_FOLDER, value):
    # Inputs: full_filename from method upload_file, UPLOAD_FOLDER path, and value it image will be sorted by
    #   0 = Hue, 1 = Luminosity, 2 = Saturation
    # Outputs: file location of sorted image

    image = Image.open(filepath)
    pixel_array = image.convert("RGB").getdata()  # Pixels are represented by their RGB values in an array
    width, height = image.size
    color_array = list(pixel_array)

    hls(color_array)  # Converts RGB value into HLS values

    quickSort(color_array, 0, len(color_array) - 1, value)  # Sorts color_array by value

    rgb(color_array)  # Converts pixel_array back to its RGB representation

    color_array = np.array(color_array).astype(np.uint8).reshape(width, height, 3)  # color_array transformed into a
                                                                                    # 3D matrix.
    outputImage = Image.fromarray(color_array, 'RGB')   # Saves sorted image
    sorted_name = f'{UPLOAD_FOLDER}/sorted_image.jpg'
    outputImage.save(sorted_name)

    return sorted_name


## Source: https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        images = False
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                value = int(request.form["sort_attribute"])  # Fetches radio button input from upload.html
                sorted_image = image_sort(filepath, UPLOAD_FOLDER, value)
                images = (filepath, sorted_image)
    finally:
        return render_template("upload.html", images=images)


@app.route('/upload/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == '__main__':
    app.run(debug=True)
