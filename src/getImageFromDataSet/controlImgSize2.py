# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import os
from PIL import Image
dataPath = "F:/研究生/图像数据/数据/其它/celebA/Img/resize/rectangle/smile/"
# dataPath = "F:/研究生/图像数据/数据/其它/celebA/test/"
# dataPath = "F:/test/"
# movePath = "F:/研究生/图像数据/数据/其它/celebA/Img/resize/rectangle/noSmile/"
list = os.listdir(dataPath)
j = 0
for i in range(0, len(list)):
    imgName = os.path.basename(list[i])
    if (os.path.splitext(imgName)[1] != ".jpg"): continue
    # image = face_recognition.load_image_file(dataPath+imgName)
    img = Image.open(dataPath+imgName)
    img.close()
    if (img.size[0] < 200 ) and (img.size[1]) < 200:
        os.remove(dataPath+imgName)






