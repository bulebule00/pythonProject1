#!/usr/bin/python
# -*- coding:utf8 -*-

import os
from api import *


if __name__ == '__main__':
    c='C:/1/test.log'
    target_file = 'C:/1/target_file'
    files=[]
    for root, dirs, files in os.walk(c):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件
    for file in files:
        convert(root+'/'+file,target_file)







