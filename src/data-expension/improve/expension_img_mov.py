# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import os
import shutil
import glob
import tensorflow as tf


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


if __name__ == '__main__':
    input_path = "E:/file/xuqiang/imagedata/"
    output_path = extend_img_in_every_folder(input_path, 512, 512, 512, 512)
    tofolder_path = "E:/file/xuqiang/all/"
    move_all_data_to_floder(output_path, tofolder_path)
