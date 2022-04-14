import urllib.request
import io
from PIL import Image
from tqdm import tqdm
import random
import sys
from copy import copy
import ssl
import certifi

K = sys.argv[2]
file_name = 'dog.jpg'

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

def k_means(URL):
    i = 0
    # f = image_file 
    f = io.BytesIO(urllib.request.urlopen(URL).read())
    img = Image.open(f) 
    pix = img.load()
    initial_means = []
    while len(initial_means) != K:
        x = random.randrange(img.size[0])
        y = random.randrange(img.size[1])
        current_color = pix[x, y]
        if len(initial_means) == 0:
            initial_means.append((x, y, current_color[0], current_color[1], current_color[2]))
        else:
            add = True
            for pixel in initial_means:
                compareToColor = (pixel[2], pixel[3], pixel[4])
                if current_color == compareToColor:
                    add = False
            if add:
                initial_means.append((x, y, current_color[0], current_color[1], current_color[2]))
    old_means = [[(0, 0, 0, 0, 0)] for x in range(5)]
    current_means = [[pixel] for pixel in initial_means]
    while current_means != old_means:
        old_means = copy(current_means)
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                current_color = pix[x, y]
                r1, g1, b1 = current_color
                mean_diffs = []
                for mean in current_means:
                    r2, g2, b2 = mean[0][2], mean[0][3], mean[0][4]
                    mean_diffs.append((((r2-r1)**2.0) + ((g2-g1)**2.0) + ((b2-b1)**2.0)))
                mean_to_put = mean_diffs.index(min(mean_diffs))
                current_means[mean_to_put].append((x, y, r1, g1, b1))
        for index, mean in enumerate(current_means):
            avgs = [0 for x in range(5)]
            size = len(mean)
            for pixel in mean:
                avgs[0] += pixel[0]
                avgs[1] += pixel[1]
                avgs[2] += pixel[2]
                avgs[3] += pixel[3]
                avgs[4] += pixel[4]
            avgs[0] = avgs[0]/size
            avgs[1] = avgs[1]/size
            avgs[2] = avgs[2]/size
            avgs[3] = avgs[3]/size
            avgs[4] = avgs[4]/size
            current_means[index] = [(round(avgs[0]), round(avgs[1]), round(avgs[2]), round(avgs[3]), round(avgs[4]))]
        old_mean_new_mean = []
        for index, mean in enumerate(current_means):
            for first_mean in mean:
                diff = ((first_mean[2] - old_means[index][0][2])**2) + ((first_mean[3] - old_means[index][0][3])**2) + ((first_mean[4] - old_means[index][0][4])**2)
                old_mean_new_mean.append(diff)
        print("Difference in means", i, ":", old_mean_new_mean)
        if not any(old_mean_new_mean):
            break
        i += 1
    for x in range(img.size[0]):
            for y in range(img.size[1]):
                current_color = pix[x, y]
                r1, g1, b1 = current_color
                mean_diffs = []
                for mean in current_means:
                    r2, g2, b2 = mean[0][2], mean[0][3], mean[0][4]
                    mean_diffs.append((((r2-r1)**2.0) + ((g2-g1)**2.0) + ((b2-b1)**2.0)))
                mean_to_put = mean_diffs.index(min(mean_diffs))
                pix[x, y] = (current_means[mean_to_put][0][2], current_means[mean_to_put][0][3], current_means[mean_to_put][0][4])
                current_means[mean_to_put].append((x, y, r1, g1, b1))
    img.show()
    return current_means

k_means(sys.argv[1])


