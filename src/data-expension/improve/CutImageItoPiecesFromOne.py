# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
from PIL import Image
import os
import glob


extensions = ['jpg']
file_list = []
#     parent_path = os.path.dirname(input_path + os.path.sep + "../")
path = "F:/研究生/图像数据/数据/其它/cycleGAN_database/maps/maps/train/resized/"
savePath = "F:/研究生/图像数据/数据/其它/cycleGAN_database/maps/maps/segment/"
for extension in extensions:
    file_glob = os.path.join(path, '*.' + extension)
    # get all the images of one folder of the input_path
    file_list.extend(glob.glob(file_glob))
for img in file_list:
    img_name = os.path.basename(os.path.splitext(img)[0])
    img_suffix = os.path.splitext(img)[1]
    image = Image.open(img)
    width = image.size[0]  # 图片大小
    height = image.size[1]
    # width_num = int(width / 2000)
    # height_num = int(height / 2000)
    # if (width_num <= 0 or height_num <= 0):
    #     box = (0, 0, width, height)
    #     img_resize = image.crop(box)
    #     img_resize.save(path + img_name + img_suffix)
    # 自己的图片扩充2*2=4倍
    flag = True
    for i in range(256, width+1, 256):
        for j in range(256, height+1, 256):
            box = (i - 256, j - 256, i, j)
            img_resize = image.crop(box)
            if flag:
                img_resize.save(savePath+"A/" + "A"+"-"+img_name + img_suffix)
                flag = False
            elif not flag:
                img_resize.save(savePath+"B/" + "B"+"-"+img_name + img_suffix)



            # if __name__ == "__main__":
            #     input_path = "E:/file/xuqiang/data/"
            #     output_path = "E:/file/xuqiang/all/"
            #     cutImage(input_path,output_path)

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
