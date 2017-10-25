# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import time

#
#
# def distort_color(image,color_ordering=0):
#     if color_ordering == 0:
#         image = tf.image.random_brightness(image,max_delta=32.0/255)
#         image = tf.image.random_saturation(image,lower=0.5,upper=1.5)
#         image = tf.image.random_flip_up_down(image,seed=1)
#         image = tf.image.random_flip_left_right(image)
#         image = tf.image.random_hue(image,max_delta=0.2)
#         image = tf.image.random_contrast(image,lower=0.5,upper=1.5)
#     elif color_ordering == 1:
#         image = tf.image.random_saturation(image, lower=0.5, upper=1.5)
#         image = tf.image.random_brightness(image, max_delta=32.0 / 255)
#         image = tf.image.random_flip_left_right(image)
#         image = tf.image.random_contrast(image, lower=0.5, upper=1.5)
#         image = tf.image.random_hue(image, max_delta=0.2)
#         image = tf.image.random_flip_up_down(image, seed=1)
#     elif color_ordering == 2:
#         image = tf.image.random_flip_left_right(image)
#         image = tf.image.random_contrast(image, lower=0.5, upper=1.5)
#         image = tf.image.random_hue(image, max_delta=0.2)
#         image = tf.image.random_saturation(image, lower=0.5, upper=1.5)
#         image = tf.image.random_brightness(image, max_delta=32.0 / 255)
#     return tf.clip_by_value(image,0.0,1.0)
#
# def preprocess_for_train(image,height,width,bbox):
#     #如果bbox没有提供，默认关注整个图像
#     if bbox is None:
#         bbox = tf.constant([0.0,0.0,1.0,1.0],dtype=tf.float32,shape=[1,1,4])
#     if image.dtype != tf.float32:
#         image = tf.image.convert_image_dtype(image,dtype=tf.float32)
#     bbox_begin,bbox_end,_ = tf.image.sample_distorted_bounding_box(tf.shape(image),bounding_boxes=bbox)
#     #截取图片
#     distorted_image = tf.slice(image,bbox_begin,bbox_end)
#     #改变图片大小为指定
#     distorted_image = tf.image.resize_images(distorted_image,[height,width],method=np.random.randint(4))
#     #变换图片
#     distorted_image = distort_color(image,np.random.randint(3))
#     return distorted_image
if __name__ == '__main__':
    start = time.time()
    print("beging....")
    # images = gafid.getFileName("../../../data/input/images/")
    path = "E:/programdate/pythonAll/DCGAN-tensorflow-master/data/inputG/"
    # images = gafid.getFileName(path)
    for root, dirs, images in os.walk(path):
        num_images = len(images)
        j = 0
        print("共有：" + str(num_images) + "图片")
        with tf.Session() as sess:
            k = 0
            for i in images:
                k = k + 1
                image_name = os.path.splitext(i)[0]
                image_suffix = os.path.splitext(i)[1]
                image_path = path + i
                image_raw_data = tf.gfile.FastGFile(image_path, 'rb').read()
                img_data = tf.image.decode_jpeg(image_raw_data)
                img_data = tf.image.resize_images(img_data, [126, 126], method=1)
                for i in range(30):
                    for j in range(30):
                        img_5 = tf.image.crop_to_bounding_box(img_data, j, i, 96, 96)
                        img_5 = tf.image.random_flip_up_down(img_5)
                        img_5 = tf.image.random_flip_left_right(img_5)
                        result = tf.image.convert_image_dtype(img_5, dtype=tf.uint8)
                        result = tf.image.encode_jpeg(result)
                        with tf.gfile.GFile(
                                                                "E:/programdate/pythonAll/DCGAN-tensorflow-master/data/outputG/" + image_name + str(
                                                        i) + str(j) + ".jpg", 'wb') as f:
                            f.write(result.eval())
                print(str(k) + " done...")
            end = time.time()
            print("耗时：" + str(end - start))
