# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
f = open("F:/研究生/图像数据/数据/其它/celebA/Anno/list_attr_celeba.txt")
newTxt = "smile.txt"
newf = open(newTxt, "a+")
newNoTxt = "noSmile.txt"
newNof = open(newNoTxt, "a+")

line = f.readline()
line = f.readline()
line = f.readline()
while line:
    array = line.split()
    if (array[0] == "000001.jpg"): print(array[32])

    if (array[32] == "-1"):
        new_context = array[0] + '\n'
        newNof.write(new_context)
    else:
        new_context = array[0] + '\n'
        newf.write(new_context)
    line = f.readline()

lines = len(newf.readlines())
print ("There are %d lines in %s" % (lines, newTxt))
lines = len(newNof.readlines())
print ("There are %d lines in %s" % (lines, newNoTxt))

f.close()
newf.close()
newNof.close()
