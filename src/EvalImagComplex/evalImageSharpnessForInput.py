# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import os
import numpy as np
from skimage import exposure,data
from skimage import io
import math
import glob
import random

def oneImageShapeness(inputPath):
    imgOne = io.imread(inputPath, as_grey=False)
    imgOneTotal =imgOne[:,:,0]+imgOne[:,:,1]+imgOne[:,:,2]
    imgGrey = np.divide(imgOneTotal,3*256)

    # print(imgGrey.shape)
    width = imgGrey.shape[0]
    heigh = imgGrey.shape[1]
    # print(width)
    # print(heigh)
    brennerValue = 0.0
    num = 0
    for i in range(width-2):
        for j in range(heigh):
            # print(str(i)+'-----'+str(j))
            brennerValue += math.pow((imgGrey[i+2,j]-imgGrey[i,j]),2)
            num = num + 1
    return brennerValue

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
        # list_file_name.extend([dir_name])
        extensions = ['jpg']
        file_list_all = []
        for extension in extensions:
            file_glob = os.path.join(inputPth, dir_name,  '*.' +extension )
            file_dict[dir_name + extension] = glob.glob(file_glob)
            file_list_all.extend(glob.glob(file_glob))
        print(dir_name + "文件底下共有图像" + str(len(file_list_all)) + "张")
        folderName= dir_name
        list_one_fakeA = file_list_all

        list_len = len(list_one_fakeA)

        brener_one_fakeA = []

        for i in list_one_fakeA:
            brener_one_fakeA.append(oneImageShapeness(i))

        average_brener_one_fakeA = np.sum(brener_one_fakeA) / list_len


        print(folderName + "的平均清晰度为：" + str(average_brener_one_fakeA))

if __name__ == "__main__":
     # inputFolderPath = "../data-caculate-complex/"
     # inputFolderPath = "F:/研究生/图像数据/数据/其它/calculate/calculate-shapness/"
     # inputFolderPath = "F:/研究生/图像数据/数据/其它/calculate/calculate-input-sharpness/zebra/"
     inputFolderPath = "F:/converImgtoTensor/data-training/"
     # inputFolderPath = "F:/研究生/图像数据/数据/其它/onetomany/"
     dateSetApart(inputFolderPath)
