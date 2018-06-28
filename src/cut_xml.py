#-*- coding=utf-8 -*-

import xml.etree.ElementTree as ET
from PIL import Image
import os
import glob
def read_xml(in_path):
    '''''读取并解析xml文件
      in_path: xml路径
      return: ElementTree'''
    tree = ET.ElementTree()
    tree.parse(in_path)
    return tree

def cut_img(in_path,save_path):
    '''
    :param in_path: the path of input images
    :param save_path: the path of save path of images
    :return: NONE
    '''

    extends = ['jpg']
    file_list = []
    for extend in extends:
        file_glob = os.path.join(in_path,'*.'+extend)
        file_list.extend(glob.glob(file_glob))

    for img_path in file_list:
        # cut the images
        im = Image.open(img_path)
        base_name = os.path.basename(img_path)
        image_name = base_name.split(".")
        name = image_name[0]
        suffix = image_name[1]
        new_name1 = name+"_1."+suffix
        new_name2 = name+"_2."+suffix
        # 截取图片1
        x = 0
        y = 0
        w = 1080
        h = 1080
        region = im.crop((x, y, x + w, y + h))
        region.save(os.path.join(save_path,new_name1))
        # 截取图片2
        x = 840
        y = 0
        w = 1080
        h = 1080
        region = im.crop((x, y, x + w, y + h))
        region.save(os.path.join(save_path,new_name2))


def cut_xml(in_path,save_path):
    extends = ['xml']
    xml_file_list = []
    for extend in extends:
        file_glob = os.path.join(in_path, '*.' + extend)
        xml_file_list.extend(glob.glob(file_glob))
    for xml_file in xml_file_list:
        base_name = os.path.basename(xml_file)
        image_name = base_name.split(".")
        name = image_name[0]
        suffix = image_name[1]
        new_name1 = name + "_1." + suffix
        new_name2 = name + "_2." + suffix

        # 1. 读取xml文件
        tree1 = read_xml(xml_file)
        tree2 = read_xml(xml_file)
        root1 = tree1.getroot()
        root2 = tree2.getroot()

        # alter filename
        for name in root1.findall("filename"):
            new_name_text = name.text.split(".")
            new_name_text = new_name_text[0] + "_1" + new_name_text[1]
            name.text = new_name_text

        # alter filename
        for name in root2.findall("filename"):
            new_name_text = name.text.split(".")
            new_name_text = new_name_text[0] + "_2" + new_name_text[1]
            name.text = new_name_text

        # alter width
        for name in root1.findall("size"):
            rank = name.find('width')
            rank.text = "1080"

        # alter width
        for name in root2.findall("size"):
            rank = name.find('width')
            rank.text = "1080"

        for country1 in root1.findall('object'):
            for x in country1.findall('bndbox'):
                rank = int(x.find('xmax').text)
                if rank >= 1080:
                    root1.remove(country1)
        tree1.write(os.path.join(save_path,new_name1))

        for country2 in root2.findall('object'):
            for x in country2.findall('bndbox'):
                rank = int(x.find('xmin').text)
                if rank <= 840:
                    root2.remove(country2)
        tree2.write(os.path.join(save_path,new_name2))









if __name__ == "__main__":
    # img_in_path = "./input/original"
    # img_out_path = "./output/original"
    # cut_img(img_in_path,img_out_path)

    xml_in_path = "./input/Annotation"
    xml_out_path = "./output/Annotation"
    cut_xml(xml_in_path,xml_out_path)











