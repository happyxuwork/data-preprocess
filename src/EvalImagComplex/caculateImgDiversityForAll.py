# -*- coding: UTF-8 -*-
'''
@author: xuqiang
随机取两张图像a1,a2,计算他们之间的欧式距离d（a1,a2）,
重复4次，取平均值，平均值越大，多样性越高
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
    arrPow2 = np.power(arrSub,2)
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
        extensions = ['fakeA','fakeB']
        file_list_all = []
        for extension in extensions:
            file_glob = os.path.join(inputPth,dir_name,extension+'*'+'.jpg')
            file_dict[dir_name+extension] = glob.glob(file_glob)
            file_list_all.extend(glob.glob(file_glob))
        print(dir_name+"文件底下共有图像"+str(len(file_list_all))+"张")
        folderName = dir_name

        list_one_fakeA = file_dict[folderName + 'fakeA']
        list_one_fakeB = file_dict[folderName + 'fakeB']

        density_one_fakeA = []
        density_one_fakeB = []
        diversity_one_fakeA = []
        diversity_one_fakeB = []
        for i in range(15):
            arrLen = len(list_one_fakeA)
            index1 = random.randint(0, (arrLen - 1))
            index2 = random.randint(0, (arrLen - 1))
            while index1 == index2:
                index2 = random.randint(0, (arrLen - 1))
            list_one_fakeA_copy = list_one_fakeA.copy()
            list_one_fakeB_copy = list_one_fakeB.copy()

            diversity_one_fakeA.append(calculateODisBetweenTwoImages(list_one_fakeA[index1], list_one_fakeA[index2]))
            diversity_one_fakeB.append(calculateODisBetweenTwoImages(list_one_fakeB[index1], list_one_fakeB[index2]))


            del list_one_fakeA_copy[index1]
            del list_one_fakeB_copy[index1]


            density_one_fakeA.append(nearestImageDisInOneSet(list_one_fakeA[index1], list_one_fakeA_copy))
            density_one_fakeB.append(nearestImageDisInOneSet(list_one_fakeB[index1], list_one_fakeB_copy))


        sum_density_one_fakeA = np.sum(density_one_fakeA)
        sum_density_one_fakeB = np.sum(density_one_fakeB)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(folderName + "中fakeA集合的密度值: " + str(sum_density_one_fakeA) + "   " + folderName + "中fakeB集合的密度值: " + str(sum_density_one_fakeB))

        sum_diversity_one_fakeA = np.sum(diversity_one_fakeA)
        sum_diversity_one_fakeB = np.sum(diversity_one_fakeB)
        print(folderName + "中fakeA集合的多样性值: " + str(sum_diversity_one_fakeA) + "   " + folderName + "中fakeB集合的多样性值: " + str(sum_diversity_one_fakeB))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")


if __name__ == "__main__":
    inputFolderPath = "F:/研究生/图像数据/数据/其它/selfCombine/noSmiletosmile/"
    dateSetApart(inputFolderPath)
    # nearestImageDisInOneSet("../data-caculate-complex/fakeA_100_0.jpg","../data-caculate-complex/demo/")