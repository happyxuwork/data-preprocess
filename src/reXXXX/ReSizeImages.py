# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
from Graphics import Graphics as gra

from PIL import Image
import shutil
import os
import glob
import time


def fixed_size(width, height, input_path, output_path):
    """按照固定尺寸处理图片"""
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        # 获得当前文件夹
        # base_name = os.path.basename(sub_dir)
        # 获取当前目录下有效的图片文件
        extensions = ['jpg']
        file_list = []
        for extension in extensions:
            file_glob = os.path.join(sub_dir, '*.' + extension)
            # get all the images of one folder of the input_path
            file_list.extend(glob.glob(file_glob))
        for image in file_list:
            im = Image.open(image)
            out = im.resize((width, height), Image.ANTIALIAS)
            image_name = os.path.basename(os.path.splitext(image)[0])
            image_suffix = os.path.splitext(image)[1]
            out.save(output_path + image_name + image_suffix)
            out = None
            im = None
        #time.sleep(1)

        # im = Image.open(图像位置)
        # out = im.resize((width, height), Image.ANTIALIAS)
        # out.save(输出位置)


if __name__ == "__main__":
    # gra.fixed_size(500, 500)
    # input_path = "E:/file/python/data/"
    # output_path = "E:/file/python/all/"



    input_path = "F:/研究生/图像数据/数据/其它/celebA/Img/resize/rectangle/smile/"
    output_path = "F:/研究生/图像数据/数据/其它/celebA/Img/resize/rectangleto256/smile/"

    fixed_size(256, 256, input_path, output_path)
