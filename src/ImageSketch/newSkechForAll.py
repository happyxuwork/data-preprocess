from scipy import misc
import numpy as np
from PIL import Image
import shutil
import glob
import time
import os
def sketch(img, threshold):
    '''
    素描
    param img: Image实例
    param threshold: 介于0到100
    '''
    if threshold < 0: threshold = 0
    if threshold > 100: threshold = 100

    width, height = img.size
    img = img.convert('L')  # convert to grayscale mode
    pix = img.load()  # get pixel matrix

    for w in range(width):
        for h in range(height):
            if w == width - 1 or h == height - 1:
                continue

            src = pix[w, h]
            dst = pix[w + 1, h + 1]

            diff = abs(src - dst)

            if diff >= threshold:
                pix[w, h] = 0
            else:
                pix[w, h] = 255
    return img



def ConvertSkech(input_path, output_path):
    """按照固定尺寸处理图片"""
    # i = 0
    # sub_dirs = [x[0] for x in os.walk(input_path)]
    # is_root_dir = True
    # for sub_dir in sub_dirs:
    #     if is_root_dir:
    #         is_root_dir = False
    #         continue
    #     # 获得当前文件夹
    #     # base_name = os.path.basename(sub_dir)
    #     # 获取当前目录
    # 下有效的图片文件
    extensions = ['jpg']
    threshold = 30
    file_list = []
    for extension in extensions:
        file_glob = os.path.join(input_path, '*.' + extension)
        # get all the images of one folder of the input_path
        file_list.extend(glob.glob(file_glob))
    for image in file_list:
        img = Image.open(image)
        image_name = os.path.basename(os.path.splitext(image)[0])
        img = sketch(img, threshold)
        lena_L_rgb = img.convert("RGB")
        lena_L_rgb.save(output_path + image_name  + '.jpg')
        # img = Image.open(image)
        # img1 = img.convert('L')  # 图片转换成灰色
        # lena_L_rgb = img1.convert("RGB")
        # image_name = os.path.basename(os.path.splitext(image)[0])
        # image_suffix = os.path.splitext(image)[1]
        # misc.imsave(output_path + image_name + image_suffix, lena_L_rgb)

if __name__ == "__main__":
    # input_path = "F:/fromcompany/handle/original/"
    input_path = "F:/fromcompany/handle/resizeto256/"
    output_path = "F:/fromcompany/handle/new1/"
    ConvertSkech(input_path, output_path)







