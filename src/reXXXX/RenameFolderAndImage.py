# -*- coding: UTF-8 -*-
'''
@author: xuqiang
按序号重新命名文件夹
文件夹中的图像名称：文件夹的名称+序号.jpg
'''
import os
import glob


def rename(input_path):
    # 获取所有的子文件夹
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    num_floder = 0
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        num_floder = num_floder + 1
        rename_dsc = os.path.join(input_path, str(num_floder))
        os.rename(sub_dir, rename_dsc)
        # 得到子文件夹的名称
        base_name = str(os.path.basename(rename_dsc))

        # 获取当前目录下有效的图片文件
        extensions = ['jpg']
        file_list = []
        for extension in extensions:
            file_glob = os.path.join(input_path, base_name, '*.' + extension)
            # get all the images of one folder of the input_path
            file_list.extend(glob.glob(file_glob))
        num_images = len(file_list)
        j = 0
        for i in file_list:
            j = j + 1
            name = os.path.join(input_path, base_name, str(j) + ".jpg")
            os.rename(i, os.path.join(input_path, base_name, base_name + "-" + str(j) + ".jpg"))


if __name__ == '__main__':
    input_path = "E:/file/xuqiang/imagedata/"
    rename(input_path)
