# -*- coding: UTF-8 -*-
'''
@author: xuqiang
tensorflow读取图片，解码，显示
'''
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import numpy as np
from skimage import exposure,data
from skimage import io
import math
import glob
def calculateOneImage(inputImagePath):
    img=io.imread(inputImagePath,as_grey=False)
    imgToOneDimetion=img.flatten()
    imgToOneDimetion = np.where(imgToOneDimetion <= 0,1,imgToOneDimetion)
    imgToOneDimetion = np.where(imgToOneDimetion == 255,254,imgToOneDimetion)
    imgNormal = np.divide(imgToOneDimetion,255)
    length = imgNormal.shape[0]
    # print(length)
    G0 = 0.0
    G1 = 0.0
    G2 = 0.0
    G0Coe = -1/(length*math.log(2))
    G1Coe = (2*math.sqrt(math.e))/(length*(math.e - 1))
    G2Coe = 4/length
    for i in range(length):
        G0 = G0 + (imgNormal[i]*math.log(imgNormal[i])+(1-imgNormal[i])*math.log((1-imgNormal[i])))
        if imgNormal[i] <= 0.5:
            G1 = G1+(imgNormal[i]*(math.pow(math.e,1-imgNormal[i])-math.pow(math.e,imgNormal[i]-1)))
        else:
            G1 = G1+((1- imgNormal[i])*(math.pow(math.e,imgNormal[i])-math.pow(math.e,-imgNormal[i])))
        G2 = G2+imgNormal[i]*(1-imgNormal[i])
    G0value = G0*G0Coe
    G1value = G1*G1Coe
    G2value = G2*G2Coe
    return G0value,G1value,G2value

def calculateFolderImage(input_path):
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    num_floder = 0
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        dir_name = os.path.basename(sub_dir)
        # num_floder = num_floder + 1
        # rename_dsc = os.path.join(input_path, str(num_floder))
        # os.rename(sub_dir, rename_dsc)
        # # 得到子文件夹的名称
        # base_name = str(os.path.basename(rename_dsc))

        extensions = ['jpg']
        file_list = []
        for extension in extensions:
            file_glob = os.path.join(input_path,dir_name, '*.' + extension)
            file_list.extend(glob.glob(file_glob))
        num_images = len(file_list)
        print("++++++++++++++++++++++++++++++++++++++")
        print(dir_name+"文件夹底下共"+str(num_images)+"张图像")
        listG0 = []
        listG1 = []
        listG2 = []
        for i in file_list:
            g0,g1,g2 = calculateOneImage(i)
            listG0.append(g0)
            listG1.append(g1)
            listG2.append(g2)
        print(dir_name+"的G0至为："+str(sum(listG0)/len(listG0)))
        print(dir_name+"的G1至为："+str(sum(listG1)/len(listG1)))
        print(dir_name+"的G2至为："+str(sum(listG2)/len(listG2)))
        print((sum(listG0) + sum(listG1) + sum(listG2)) / (3*len(listG2)))
        print(dir_name + "文件夹处理完毕")
        print("++++++++++++++++++++++++++++++++++++++")
if __name__ == "__main__":
    # inputFolderPath = "./data/other/"
    # inputFolderPath = "F:/caculateComplex/marble2marble-20-250/"
    # inputFolderPath = "F:/研究生/图像数据/数据/其它/cityscapes/caculateComplex/"
    # inputFolderPath = "F:/研究生/图像数据/数据/其它/calculate/"
    # inputFolderPath = "G:/桌面引用/待办事情/小论文图像/拼图/"
    # inputFolderPath = "F:/研究生/图像数据/数据/其它/selfCombine/noSmiletosmile/"
    # inputFolderPath = "F:/caculateComplex/segment/"
    # inputFolderPath = "F:/研究生/图像数据/数据/其它/edges2shoes/edges2shoes/segmentTrain/"
    # inputFolderPath = "F:/研究生/图像数据/数据/其它/edges2handbags/test/"
    inputFolderPath = "F:/研究生/图像数据/数据/其它/edges2handbags/edges2handbags/segmentVal/"
    calculateFolderImage(inputFolderPath)




