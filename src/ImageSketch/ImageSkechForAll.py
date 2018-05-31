from scipy import misc
import numpy as np
from PIL import Image
import shutil
import glob
import time
import os
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
    #     # 获取当前目录下有效的图片文件
    extensions = ['jpg']
    file_list = []
    for extension in extensions:
        file_glob = os.path.join(input_path, '*.' + extension)
        # get all the images of one folder of the input_path
        file_list.extend(glob.glob(file_glob))
    for image in file_list:
        img = Image.open(image)
        img1 = img.convert('L')  # 图片转换成灰色
        lena_L_rgb = img1.convert("RGB")
        image_name = os.path.basename(os.path.splitext(image)[0])
        image_suffix = os.path.splitext(image)[1]
        misc.imsave(output_path + image_name + image_suffix, lena_L_rgb)

if __name__ == "__main__":
    # input_path = "F:/fromcompany/handle/original/"
    input_path = "F:/fromcompany/handle/resizeto256/"
    output_path = "F:/fromcompany/handle/skech/"
    ConvertSkech(input_path, output_path)







