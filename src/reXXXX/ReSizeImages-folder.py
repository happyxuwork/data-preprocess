# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
from Graphics import Graphics as gra
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from PIL import Image
import shutil
import os
import glob
import time


def fixed_size(width, height, input_path, output_path):
    # """按照固定尺寸处理图片"""
    i = 0
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        # 获得当前文件夹
        base_name = os.path.basename(sub_dir)
    #     # 获取当前目录下有效的图片文件
        extensions = ['jpg','jpeg']
        file_list = []
        for extension in extensions:
            file_glob = os.path.join(input_path,base_name, '*.' + extension)
            # get all the images of one folder of the input_path
            file_list.extend(glob.glob(file_glob))
        for image in file_list:
            im = Image.open(image).convert('RGB')
            out = im.resize((width, height), Image.ANTIALIAS)
            # image_name = os.path.basename(os.path.splitext(image)[0])
            image_suffix = os.path.splitext(image)[1]
            out.save(output_path + str(i) + image_suffix)
            i = i + 1
            out = None
            im = None
        # time.sleep(1)

        # im = Image.open(图像位置)
        # out = im.resize((width, height), Image.ANTIALIAS)
        # out.save(输出位置)


if __name__ == "__main__":
    # gra.fixed_size(500, 500)
    # input_path = "E:/file/python/data/"0
    # output_path = "E:/file/python/all/"



    input_path = "F:\\fromcompany\\图片情感分类1\\图片情感分类\\"
    output_path = "F:\\fromcompany\\图片情感分类1\\handle\\"

    fixed_size(512, 512, input_path, output_path)
