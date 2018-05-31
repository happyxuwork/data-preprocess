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
        extensions = ['fakeA', 'fakeB']
        file_list_all = []
        for extension in extensions:
            file_glob = os.path.join(inputPth, dir_name, extension + '*' + '.jpg')
            file_dict[dir_name + extension] = glob.glob(file_glob)
            file_list_all.extend(glob.glob(file_glob))
        print(dir_name + "文件底下共有图像" + str(len(file_list_all)) + "张")
        folderName= dir_name
        list_one_fakeA = file_dict[folderName + 'fakeA']
        list_one_fakeB = file_dict[folderName + 'fakeB']
        list_len = len(list_one_fakeA)

        brener_one_fakeA = []
        brener_one_fakeB = []
        for i, j in zip(list_one_fakeA, list_one_fakeB):
            brener_one_fakeA.append(oneImageShapeness(i))
            brener_one_fakeB.append(oneImageShapeness(j))
        average_brener_one_fakeA = np.sum(brener_one_fakeA) / list_len
        average_brener_one_fakeB = np.sum(brener_one_fakeB) / list_len

        print(folderName + "中fakeA集合的平均清晰度为：" + str(average_brener_one_fakeA))
        print(folderName + "中fakeB集合的平均清晰度为：" + str(average_brener_one_fakeB))





    # folderOne = list_file_name[0]
    # folderTwo = list_file_name[1]
    # list_one_fakeA = file_dict[folderOne + 'fakeA']
    # list_one_fakeB = file_dict[folderOne + 'fakeB']
    # list_two_fakeA = file_dict[folderTwo + 'fakeA']
    # list_two_fakeB = file_dict[folderTwo + 'fakeB']
    #
    # list_len = len(list_one_fakeA)
    #
    #
    # brener_one_fakeA = []
    # brener_one_fakeB = []
    # brener_two_fakeA = []
    # brener_two_fakeB = []
    # for i,j,k,l in zip(list_one_fakeA,list_one_fakeB,list_two_fakeA,list_two_fakeB):
    #     brener_one_fakeA.append(oneImageShapeness(i))
    #     brener_one_fakeB.append(oneImageShapeness(j))
    #     brener_two_fakeA.append(oneImageShapeness(k))
    #     brener_two_fakeB.append(oneImageShapeness(l))
    # average_brener_one_fakeA = np.sum(brener_one_fakeA)/list_len
    # average_brener_one_fakeB = np.sum(brener_one_fakeB)/list_len
    # average_brener_two_fakeA = np.sum(brener_two_fakeA)/list_len
    # average_brener_two_fakeB = np.sum(brener_two_fakeB)/list_len
    #
    # print(folderOne+"中fakeA集合的平均清晰度为："+str(average_brener_one_fakeA))
    # print(folderOne+"中fakeB集合的平均清晰度为："+str(average_brener_one_fakeB))
    # print(folderTwo+"中fakeA集合的平均清晰度为："+str(average_brener_two_fakeA))
    # print(folderTwo+"中fakeB集合的平均清晰度为："+str(average_brener_two_fakeB))
    #
    # if average_brener_one_fakeA >= average_brener_two_fakeA:
    #     print(folderOne+"中fakeA集合的清晰度高于"+folderTwo)
    # else:
    #     print(folderOne + "中fakeA集合的清晰度低于" + folderTwo)
    #
    # if average_brener_one_fakeB >= average_brener_two_fakeB:
    #     print(folderOne+"中fakeB集合的清晰度高于"+folderTwo)
    # else:
    #     print(folderOne + "中fakeB集合的清晰度低于" + folderTwo)

if __name__ == "__main__":
     # inputFolderPath = "../data-caculate-complex/"
     # inputFolderPath = "F:/研究生/图像数据/数据/其它/calculate/补充/calculate-shapness/"
     inputFolderPath = "F:/研究生/图像数据/数据/其它/selfCombine/noSmiletosmile/"
     #inputFolderPath = "F:/研究生/图像数据/数据/其它/onetomany/"
     # inputFolderPath = "F:/研究生/图像数据/数据/其它/onetomany/"
     dateSetApart(inputFolderPath)
