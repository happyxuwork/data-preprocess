# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import shutil
import os

'''
用于返回最新的目录
'''
def getNewestFile(fileNameList):
    sortList = sorted(fileNameList)
    listLen = len(fileNameList)
    return sortList[listLen-1]

def moveTheFile(sorceDir,targetDir):
    taskDirs = [x for x in os.listdir(sorceDir)]
    for taskDir in taskDirs:
        print(os.path.join(sorceDir,taskDir))
        factorDirs = [y for y in os.listdir(os.path.join(sorceDir,taskDir))]
        for factorDir in factorDirs:
            newestCheckPoinFileList = [z for z in os.listdir(os.path.join(sorceDir,taskDir,factorDir))]
            newestCheckPoinFile = getNewestFile(newestCheckPoinFileList)
            filNeedPath = os.path.join(sorceDir,taskDir,factorDir,newestCheckPoinFile)
            print(filNeedPath)
            # needFileExtension = ['checkpoint','cyclegan-199.data-00000-of-00001','cyclegan-199.index','cyclegan-199.meta']
            needFileExtension = ['1.txt','2.txt']
            os.makedirs(os.path.join(targetDir, taskDir, factorDir))
            for extension in needFileExtension:
                print(os.path.join(filNeedPath,extension))

                shutil.copy(os.path.join(filNeedPath,extension), os.path.join(targetDir,taskDir,factorDir,extension))




        # print(newestSecondFile)
        # newestSecondFile = getNewestFile(secondDirs)
        # fileInter = [z for z in os.listdir(os.path.join(sorceDir, dir,newestSecondFile))]
        # if file


    # newestFile = getNewestFile(dirs)
    # print(newestFile)


if __name__ == "__main__":
    # sourceDir = "F:/1/cyclegan-188.data-00000-of-00001"
    sourceDir = "G:/demo/"
    targetDir = "G:/to/"
    moveTheFile(sourceDir,targetDir)


    # print(getNewestFile(list))


# shutil.copy(sourceDir,  targetDir)