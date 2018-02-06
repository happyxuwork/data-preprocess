# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import os
import shutil

nof = open("noSmile.txt")
hasf = open("smile.txt")

noLine = nof.readline()
hasLine = hasf.readline()
# dataPath = "F:/研究生/图像数据/数据/其它/celebA/Img/img_align_celeba/img_align_celeba/"
dataPath = "F:/研究生/图像数据/数据/其它/celebA/Img/test/"
movePath = "F:/研究生/图像数据/数据/其它/celebA/Img/handle/smileOrNot/"
list = os.listdir(dataPath)
hasGo = True
noGo = True
for i in range(0, len(list)):
    imgName = os.path.basename(list[i])
    # if (os.path.splitext(imgName)[1] != ".jpg"): continue

    noArray = noLine.split()
    if (len(noArray) < 1): noGo = False
    hasArray = hasLine.split()
    if (len(hasArray) < 1): hasGo = False

    if (noGo and (imgName == noArray[0])):
        oldname= dataPath+imgName
        newname=movePath+"noSmile/"+imgName
        shutil.move(oldname, newname)
        noLine = nof.readline()
    elif (hasGo and (imgName == hasArray[0])):
        oldname= dataPath+imgName
        newname=movePath+"smile/"+imgName
        shutil.move(oldname, newname)
        hasLine = hasf.readline()

    if (i % 100 == 0): print(imgName)

nof.close()
hasf.close()

