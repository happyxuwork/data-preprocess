# -*- coding: UTF-8 -*-
'''
@author: xuqiang
查看图片是否为RGB三通道的图片
'''

from PIL import Image
import shutil
import os
import glob
import time


def detective_img_or_RGB(input_path):
    # sub_dirs = [x[0] for x in os.walk(input_path)]
    # is_root_dir = True
    # for sub_dir in sub_dirs:
    #     if is_root_dir:
    #         is_root_dir = False
    #         continue
    #     # 获得当前文件夹
    #     base_name = os.path.basename(sub_dir)
    #     # 获取当前目录下有效的图片文件
    extensions = ['jpg']
    file_list = []
    for extension in extensions:
        # file_glob = os.path.join(sub_dir, '*.' + extension)
        file_glob = os.path.join(input_path, '*.' + extension)
        # get all the images of one folder of the input_path
        file_list.extend(glob.glob(file_glob))
    for image in file_list:
        im = Image.open(image)
        if im.mode != 'RGB':
            # print(os.path.basename(image))
            print(image)
            #remove it may be a good ideal
            im.close()
            os.remove(os.path.join(input_path,os.path.basename(image)))
       # r,g,b = im.split()
        # r.show()
        # g.show()
        # b.show()


        # im = Image.open(图像位置)
        # out = im.resize((width, height), Image.ANTIALIAS)
        # out.save(输出位置)


if __name__ == "__main__":

    # input_path = "F:/研究生/图像数据/数据/其它/calculate/calculate-input-sharpness/zebra/"
    # input_path = "F:/研究生/图像数据/数据/其它/celebA/Img/handle/smileOrNot/noSmile"
    input_path = "F:/swd/new2/real/"
    # os.remove('F:/fromcompany/handle/1\\苏打苏塔 (911).jpg')
    # input_path = "F:/研究生/图像数据/数据/其它/cycleGAN_database/maps/maps/segment/"
    #output_path = "E:/file/xuqiang/all-128-128/"

    detective_img_or_RGB(input_path)
