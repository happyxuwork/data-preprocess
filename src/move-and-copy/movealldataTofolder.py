# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''

# import os
# import shutil
# if __name__ == "__main__":
#     path = 'E:/data/'
#     new_path = 'E:/dls/'
#
# def move_files(path,new_path):
#     for root, dirs, files in os.walk(path):
#         if len(dirs) != 0:
#             for i in range(len(files)):
#                 if files[i][-3:-1] == 'jpg':
#                     file_path = root + '/' + files[i]
#                     new_file_path = new_path + '/' + files[i]
#                     shutil.move(file_path, new_file_path)
import os
import shutil
import glob


# move the file that you want suffix in the input_path to out_path
def moveOneToAnother(input_path, output_path):
    sub_dirs = [x[0] for x in os.walk(input_path)]
    is_root_dir = True
    for sub_dir in sub_dirs:
        if is_root_dir:
            is_root_dir = False
            continue
        # 获取当前目录下有效的图片文件
        extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
        file_list = []
        dir_name = os.path.basename(sub_dir)
        for extension in extensions:
            file_glob = os.path.join(input_path, dir_name, '*.' + extension)
            file_list.extend(glob.glob(file_glob))
        for i in file_list:
            shutil.copyfile(i, os.path.join(output_path, os.path.basename(i)))
            # shutil.copyfile(i, os.path.join(output_path, os.path.basename(i)))

if __name__ == "__main__":
    path = 'E:/data/'
    new_path = 'E:/dls/'
    moveOneToAnother(path, new_path)
