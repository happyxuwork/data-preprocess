from scipy import misc
import numpy as np
from PIL import Image
import shutil
import glob
import time
from skimage import img_as_float
import matplotlib.pyplot as plt
from skimage import io
from skimage.filters._gaussian import gaussian
import os
import scipy.misc


def ConvertSkech(input_path, output_path):
    extensions = ['jpg']
    file_list = []
    for extension in extensions:
        file_glob = os.path.join(input_path, '*.' + extension)
        # get all the images of one folder of the input_path
        file_list.extend(glob.glob(file_glob))
    for image in file_list:
        img = io.imread(image)
        img = img_as_float(img)
        I_out = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3.0
        I_invert = 1.0 - I_out
        I_gauss = gaussian(I_invert, sigma=5)
        delta = 0.0001
        I_dodge = (I_out + delta) / (1 + delta - I_gauss)
        th = 0.95
        mask = I_dodge > th
        max_val = I_dodge.max()
        I_dodge = I_dodge * (1 - mask) + (th + I_dodge / max_val * (1 - th)) * mask
        img_out = I_dodge.copy()
        image_name = os.path.basename(os.path.splitext(image)[0])
        image_suffix = os.path.splitext(image)[1]
        scipy.misc.toimage(img_out).save(output_path + image_name + image_suffix)

        # img = Image.open(image)
        # img1 = img.convert('L')  # 图片转换成灰色
        # lena_L_rgb = img1.convert("RGB")
        # image_name = os.path.basename(os.path.splitext(image)[0])
        # image_suffix = os.path.splitext(image)[1]
        # misc.imsave(output_path + image_name + image_suffix, lena_L_rgb)

if __name__ == "__main__":
    # input_path = "F:/fromcompany/handle/original/"
    input_path = "F:/fromcompany/handle/resizeto256/"
    output_path = "F:/fromcompany/handle/skechto256/"
    ConvertSkech(input_path, output_path)







