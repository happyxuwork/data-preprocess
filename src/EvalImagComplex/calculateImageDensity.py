# -*- coding: UTF-8 -*-
'''
@author: xuqiang
随机取一张图像a1，找到集合中与a1最近的图像a2，得到欧式距离d(a1,a2)
重复4次，取平均值，平均值越大，密度越小
'''
import os
import numpy as np
from skimage import exposure,data
from skimage import io
import math
import glob
import random

def calculateODisBetweenTwoImages(imgOne,imgTwo):
    imgOne = io.imread(imgOne, as_grey=False)
    imgOneToOneD = imgOne.flatten()

    imgTwo = io.imread(imgTwo, as_grey=False)
    imgTwoToOneD = imgTwo.flatten()

    arrSub = np.subtract(imgOneToOneD,imgTwoToOneD)
    arrNormal = np.divide(arrSub,255)
    arrPow2 = np.power(arrNormal,2)
    arrSum = np.sum(arrPow2)
    arrSqrt = np.sqrt(arrSum)
    return arrSqrt

def nearestImageDisInOneSet(img,imgSet):
    # setLen = len(imgSet)
    distance_dict = {}
    for i in imgSet:
        dis = calculateODisBetweenTwoImages(img,i)
        distance_dict[img+i] = dis
    # key = min(distance_dict.items(), key=lambda x: x[1])[0]
    value = min(distance_dict.items(), key=lambda x: x[1])[1]
    return value

def dateSetApart(inputPth):
    list_file_name = []
    file_dict = {}

    sub_dirs = [x[0] for x in os.walk(inputPth)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        dir_name = os.path.basename(sub_dir)
        list_file_name.extend([dir_name])
        extensions = ['jpg']
        file_list_all = []
        for extension in extensions:
            file_glob = os.path.join(inputPth,dir_name,'*.'+extension)
            file_list_all.extend(glob.glob(file_glob))
        print(dir_name+"文件底下共有图像"+str(len(file_list_all))+"张")

        density_list = []
        for i in range(60):
            arrLen = len(file_list_all)
            index1 = random.randint(0,(arrLen-1))
            file_list__all_copy = file_list_all.copy()

            del file_list__all_copy[index1]

            density_list.append(nearestImageDisInOneSet(file_list_all[index1],file_list__all_copy))

        sum_density_all = np.sum(density_list)
        print(dir_name+"--数据集的分布密度为: "+str(sum_density_all))

if __name__ == "__main__":
    inputFolderPath =  "../data-calculate-density/marble"
    dateSetApart(inputFolderPath)
    # nearestImageDisInOneSet("../data-caculate-complex/fakeA_100_0.jpg","../data-caculate-complex/demo/")