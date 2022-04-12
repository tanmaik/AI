from re import template
import urllib.request
import io
from PIL import Image

K = 8

def naive8(image_file):
    f = image_file 
    img = Image.open(f) 
    pix = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            temp = pix[x, y]
            redVal, greenVal, blueVal = 0, 0, 0
            if temp[0] >= 128:
                redVal = 255
            if temp[1] >= 128:
                greenVal = 255
            if temp[2] >= 128:
                blueVal = 255
            pix[x, y] = (redVal, greenVal, blueVal)
    img.show()
    img.save("my_image.png")

def naive27(image_file):
    f = image_file
    img = Image.open(f)
    pix = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            temp = pix[x, y]
            redVal, greenVal, blueVal = 0, 0, 0
            if temp[0] >= (255 * 2 // 3):
                redVal = 255
            elif temp[0] < (255 // 3):
                redVal = 0
            else:
                redVal = 127
            if temp[1] >= (255 * 2 // 3):
                greenVal = 255
            elif temp[1] < (255 // 3):
                greenVal = 0
            else:
                greenVal = 127
            if temp[2] >= (255 * 2 // 3):
                blueVal = 255
            elif temp[2] < (255 // 3):
                blueVal = 0
            else:
                blueVal = 127
            pix[x, y] = (redVal, greenVal, blueVal)
    img.show()
    img.save("my_image.png")


naive27('dog.jpg')

