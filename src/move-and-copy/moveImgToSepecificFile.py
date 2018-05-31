# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import os
def moveImg(sorceDir,targetDir):
    sub_dirs = [x[0] for x in os.walk(sorceDir)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue

