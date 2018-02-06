# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import shutil
import glob
import tensorflow as tf
from PIL import Image
import shutil
import os
import glob
import time


# move the file that you want suffix in the input_path to out_path
def move_all_data_to_floder(input_path, output_path):
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        # 获取当前目录下有效的图片文件
        extensions = ['jpg']
        file_list = []
        dir_name = os.path.basename(sub_dir)
        for extension in extensions:
            file_glob = os.path.join(input_path, dir_name, '*.' + extension)
            file_list.extend(glob.glob(file_glob))
        for i in file_list:
            shutil.copyfile(i, os.path.join(output_path, os.path.basename(i)))


# extend imags in evrey folder of input_path
# and save the file to the parent folder of handle
# return the output path
# parent_path = os.path.dirname(d) #获得d所在的目录,即d的父级目录
# parent_path  = os.path.dirname(parent_path) ##获得parent_path所在的目录即parent_path的父级目录
# abspath = path.abspath(d) #返回d所在目录规范的绝对路径

# python下取得父文件夹绝对路径的方法
# os.path.abspath(os.path.dirname(__file__)+os.path.sep+"..")
def extend_img_in_every_folder(input_path, resize_with, resize_heigh, out_with, out_heigh):
    output_path = os.path.dirname(input_path + os.path.sep + "../")
    return_path = os.path.abspath(output_path)
    return_path = return_path + "/handle/"
    os.mkdir(output_path + "/handle/")
    diff_with = resize_with - out_with + 1
    diff_heigt = resize_heigh - out_heigh + 1
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        base_name = os.path.basename(sub_dir)
        # 获取当前目录下有效的图片文件
        extensions = ['jpg']
        # 创建输出的文件夹
        path = output_path + "/handle/" + base_name + "/"
        os.makedirs(path)
        file_list = []
        dir_name = os.path.basename(sub_dir)
        for extension in extensions:
            file_glob = os.path.join(input_path, dir_name, '*.' + extension)
            # get all the images of one folder of the input_path
            file_list.extend(glob.glob(file_glob))

        num_images = len(file_list)
        print("文件夹：" + sub_dir + "共有：" + str(num_images) + "张图片")
        j = 0
        with tf.Session() as sess:
            for i in file_list:
                j = j + 1
                print("开始处理第：" + str(j) + "张图片...")
                image_name = os.path.basename(os.path.splitext(i)[0])
                image_suffix = os.path.splitext(i)[1]
                image_path = i
                image_raw_data = tf.gfile.FastGFile(image_path, 'rb').read()
                image_data = tf.image.decode_jpeg(image_raw_data)
                image_data = tf.image.resize_images(image_data, [resize_with, resize_heigh], method=1)
                for diff_h in range(diff_heigt):
                    for diff_w in range(diff_with):
                        img_box = tf.image.crop_to_bounding_box(image_data, diff_h, diff_w, out_heigh, out_heigh)
                        img_out = tf.image.random_flip_up_down(img_box)
                        img_out = tf.image.random_flip_left_right(img_out)
                        result = tf.image.convert_image_dtype(img_out, dtype=tf.uint8)
                        result = tf.image.encode_jpeg(result)
                        out_img_path = path + image_name + str(diff_w) + str(diff_h) + ".jpg"
                        with tf.gfile.GFile(path + image_name + str(diff_w) + str(diff_h) + ".jpg", 'wb') as f:
                            f.write(result.eval())
                print("第" + str(j) + "张图片处理完毕！！！")
            sess.close()
    print("所有文件夹中的图片已处理完毕")
    return return_path

'''
将文件夹底下的图像扩充beishu倍，然后resize到resize_with和resize_heigh
'''
def extend_multiply_img_in_every_folder(input_path,output_path,beishu,resize_with,resize_heigh):
    # # 重命名文件底下的所有文件夹及里面的图像
    # sub_dirs = [x[0] for x in os.walk(input_path)]
    # is_root_dir = True
    # num_floder = 0
    # for sub_dir in sub_dirs:
    #     if is_root_dir:
    #         is_root_dir = False
    #         continue
    #     num_floder = num_floder + 1
    #     rename_dsc = os.path.join(input_path, str(num_floder))
    #     os.rename(sub_dir, rename_dsc)
    #     # 得到子文件夹的名称
    #     base_name = str(os.path.basename(rename_dsc))
    #
    #     # 获取当前目录下有效的图片文件
    #     extensions = ['jpg']
    #     file_list = []
    #     for extension in extensions:
    #         file_glob = os.path.join(input_path, base_name, '*.' + extension)
    #         # get all the images of one folder of the input_path
    #         file_list.extend(glob.glob(file_glob))
    #     num_images = len(file_list)
    #     j = 0
    #     for i in file_list:
    #         j = j + 1
    #         name = os.path.join(input_path, base_name, str(j) + ".jpg")
    #         os.rename(i, os.path.join(input_path, base_name, base_name + str(j) + str(j) + ".jpg"))


    #扩充图像
    temp_path = os.path.dirname(input_path + os.path.sep + "../")
    return_path = os.path.abspath(temp_path)
    return_path = return_path + "/extendtmp/"
    os.mkdir(temp_path + "/extendtmp/")
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    extensions = ['jpg']
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        # 获得当前文件夹
        base_name = os.path.basename(sub_dir)
        # 获取当前目录下有效的图片文件

        file_list = []
        for extension in extensions:
            file_glob = os.path.join(sub_dir, '*.' + extension)
            # get all the images of one folder of the input_path
            file_list.extend(glob.glob(file_glob))
        for image in file_list:
            img_name = os.path.basename(os.path.splitext(image)[0])
            img_suffix = os.path.splitext(image)[1]
            image = Image.open(image)
            width = image.size[0]  # 图片大小
            height = image.size[1]
            w_step = int((width / beishu) -1)
            h_step = int((height / beishu) -1)
            for i in range(w_step, width, w_step):
                for j in range(h_step, height, h_step):
                    box = (i - w_step, j - h_step, i, j)
                    img_resize = image.crop(box)
                    img_resize.save(return_path + img_name + "-" + str(i) + str(j) + img_suffix)
    file_list = []
    for extension in extensions:
        file_glob = os.path.join(return_path, '*.' + extension)
        # get all the images of one folder of the input_path
        file_list.extend(glob.glob(file_glob))
        for image in file_list:
            im = Image.open(image)
            out = im.resize((resize_with, resize_heigh), Image.ANTIALIAS)
            image_name = os.path.basename(os.path.splitext(image)[0])
            image_suffix = os.path.splitext(image)[1]
            out.save(output_path + image_name + image_suffix)
    shutil.rmtree(return_path)
    time.sleep(2)
if __name__ == '__main__':
    #input_path = "F:/handle/origin/"
    # output_path = extend_img_in_every_folder(input_path, 256, 256, 256, 256)
    # tofolder_path = "F:/handle/originsize256/"
    # move_all_data_to_floder(output_path, tofolder_path)

    # input_path = "F:/X---Y/handleY/"
    # output_path1 = "F:/X---Y/extendY-3-3/"
    # output_path2 = "F:/X---Y/extendY-2-2/"
    # output_path3 = "F:/X---Y/extendY-1-1/"
    # extend_multiply_img_in_every_folder(input_path, output_path1, 3, 256, 256)
    # extend_multiply_img_in_every_folder(input_path, output_path2, 2, 256, 256)
    # extend_multiply_img_in_every_folder(input_path, output_path3, 1, 256, 256)

    input_path = "F:/X---Y/granite/test/testB/"
    output_path1 = "F:/X---Y/granite/extend/testB/"
    extend_multiply_img_in_every_folder(input_path, output_path1, 4, 256, 256)

    # input_path = "F:/X---Y/granite/Candidates-one/"
    # output_path1 = "F:/X---Y/granite/Candidates-one-3-3/"
    # extend_multiply_img_in_every_folder(input_path, output_path1, 3, 256, 256)

