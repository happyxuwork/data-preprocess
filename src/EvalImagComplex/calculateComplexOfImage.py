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

img=io.imread('../data/demo3.jpg',as_grey=False)
imgToOneDimetion=img.flatten()
imgToOneDimetion = np.where(imgToOneDimetion <= 0,1,imgToOneDimetion)
imgToOneDimetion = np.where(imgToOneDimetion == 255,254,imgToOneDimetion)
imgNormal = np.divide(imgToOneDimetion,255)

length = imgNormal.shape[0]
print(length)
# num = 0
# for i in range(length):
#         print(imgNormal[i])
# print(num)
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

print("G0 value:"+str(G0*G0Coe))
print("G1 value:"+str(G1*G1Coe))
print("G2 value:"+str(G2*G2Coe))
print((G0*G0Coe+G1*G1Coe+G2*G2Coe)/3)








