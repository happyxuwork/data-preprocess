# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
from PIL import Image
import os
import glob


def cutImage(input_path, output_path):
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        dir_name = os.path.basename(sub_dir)
        extensions = ['jpg']
        file_list = []
        parent_path = os.path.dirname(input_path + os.path.sep + "../")
        path = parent_path + "/extend2-2/" + dir_name + "/"
        os.makedirs(path)
        for extension in extensions:
            file_glob = os.path.join(input_path, dir_name, '*.' + extension)
            # get all the images of one folder of the input_path
            file_list.extend(glob.glob(file_glob))
        for img in file_list:
            img_name = os.path.basename(os.path.splitext(img)[0])
            img_suffix = os.path.splitext(img)[1]
            image = Image.open(img)
            width = image.size[0]  # 图片大小
            height = image.size[1]
            # 自己的图片扩充3*3=9倍
            for i in range(1032, width, 1032):
                for j in range(1032, height, 1032):
                    box = (i - 1032, j - 1032, i, j)
                    img_resize = image.crop(box)
                    img_resize.save(path + img_name + "-" + str(i) + str(j) + img_suffix)


if __name__ == "__main__":
    input_path = "F:/domainX/"
    output_path = "F:/domainX/aa23-extend/"
    cutImage(input_path, output_path)

    # img = Image.open("E:/file/xuqiang/data/哈哈/IMG_20171029_161055.jpg")
    # width = img.size[0]  # 图片大小
    # height = img.size[1]
    # for i in range(1034,width,1034):
    #     for j in range(1034,height,1034):
    #         box = (i-1034,j-1034,i,j)
    #         img2 = img.crop(box)
    #         img2.save("E:/file/xuqiang/all/IMG_20171029_161055"+"-"+str(i)+str(j)+".jpg")

    # 从左上角开始 剪切 200*200的图片
    # img2 = img.crop((1034, 2068, 2068, 3102))
    # img2.save("E:/file/xuqiang/all/IMG_20171029_16105553.jpg")
    #
    # width = img.size[0]  # 图片大小
    # height = img.size[1]
    # img3 = img.crop(
    #     (
    #         width - 1034,
    #         height - 1034,
    #         width,
    #         height
    #     )
    # )
    # img3.save("lena3.jpg")
    #
    #
    #
    # half_the_width = img.size[0] / 2
    # half_the_height = img.size[1] / 2
    # img4 = img.crop(
    #     (
    #         half_the_width - 50,
    #         half_the_height - 75,
    #         half_the_width + 50,
    #         half_the_height + 75
    #     )
    # )
    # img4.save("lena4.jpg")
    #
    # longer_side = max(img4.size)
    # horizontal_padding = (longer_side - img4.size[0]) / 2
    # vertical_padding = (longer_side - img4.size[1]) / 2
    # img5 = img4.crop(
    #     (
    #         -horizontal_padding,
    #         -vertical_padding,
    #         img4.size[0] + horizontal_padding,
    #         img4.size[1] + vertical_padding
    #     )
    # )
    # img5.save("lena5.jpg")
