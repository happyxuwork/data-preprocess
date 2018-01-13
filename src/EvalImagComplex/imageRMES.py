# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import numpy as np
from skimage import exposure,data
from skimage import io
import math
import glob
# '../data/horse2zebra-10-100\\inputA_100_0.jpg'  '../data/horse2zebra-10-100\\cycA_100_0.jpg'
def onePairImageRMSE(onePath,twoPath):
    imgOne = io.imread(onePath, as_grey=False)
    imgOneToOneD = imgOne.flatten()

    imgTwo = io.imread(twoPath, as_grey=False)
    imgTwoToOneD = imgTwo.flatten()
    # arrSub = np.subtract(imgOneToOneD,imgTwoToOneD)
    # arrPow = np.power(arrSub,2)
    # arrSum= np.sum(arrPow)
    # arrMean = np.divide(arrSum,len(imgTwoToOneD))
    # arrRESM = np.sqrt(arrMean)
    oneRESM = math.sqrt(np.sum(np.power(np.subtract(imgOneToOneD,imgTwoToOneD),2))/len(imgOneToOneD))
    return oneRESM

def twoSetImageRMSE(firstSet,secondSet):
    twoSetRMSEResult = 0.0
    if len(firstSet) != len(secondSet):
        print("when calculate twoSetImageRMSE the pair set are not same length!")
        return
    else:
        for (i,j) in zip(firstSet,secondSet):
            twoSetRMSEResult = twoSetRMSEResult + onePairImageRMSE(i,j)
        return twoSetRMSEResult/len(firstSet)

def dateSetRMSE(inputPth):
    sub_dirs = [x[0] for x in os.walk(inputPth)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        dir_name = os.path.basename(sub_dir)
        extensions = ['inputA','inputB','fakeA','fakeB','cycA','cycB']
        file_list_inputA = []
        file_list_inputB = []
        file_list_fakeA = []
        file_list_fakeB = []
        file_list_cycA = []
        file_list_cycB = []
        file_list_all = []
        file_dict = {}

        for extension in extensions:
            file_glob = os.path.join(inputPth,dir_name,extension+'*'+'.jpg')
            file_dict[extension] = glob.glob(file_glob)
            file_list_all.extend(glob.glob(file_glob))
        file_list_inputA = file_dict['inputA']
        file_list_inputB = file_dict['inputB']
        file_list_fakeA = file_dict['fakeA']
        file_list_fakeB = file_dict['fakeB']
        file_list_cycA = file_dict['cycA']
        file_list_cycB = file_dict['cycB']
        num_images = len(file_list_all)
        print("++++++++++++++++++++++++++++++++++++++")
        print(dir_name + "文件夹底下共" + str(num_images) + "张图像")
        inputA_fakeA = twoSetImageRMSE(file_list_inputA,file_list_fakeA)
        inputA_cycA = twoSetImageRMSE(file_list_inputA,file_list_cycA)

        inputB_fakeB = twoSetImageRMSE(file_list_inputB,file_list_fakeB)
        inputB_cycB = twoSetImageRMSE(file_list_inputB,file_list_cycB)

        inputA_inputB = twoSetImageRMSE(file_list_inputA,file_list_inputB)
        fakeA_fakeB = twoSetImageRMSE(file_list_fakeA,file_list_fakeB)

        print("inputA和fakeA的RMSE为："+str(inputA_fakeA))
        print("inputA和cycA的RMSE为："+str(inputA_cycA))
        print("inputB和fakeB的RMSE为："+str(inputB_fakeB))
        print("inputB和cycB的RMSE为："+str(inputB_cycB))
        print("inputA和inputB的RMSE为："+str(inputA_inputB))
        print("fakeA和fakeB的RMSE为："+str(fakeA_fakeB))




if __name__ == "__main__":
    # onePairImageRMSE('../data/horse2zebra-10-100\\inputA_100_0.jpg', '../data/horse2zebra-10-100\\cycA_100_0.jpg')
    # RMSE = onePairImageRMSE()
    # print(RMSE)
    # print(os.path.abspath("../data/horse2zebra-10-100/"))
    dateSetRMSE("../data/")




