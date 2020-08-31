#!/usr/bin/python
# -*- coding:utf8 -*-

import os
from api import *
from random import *



if __name__ == '__main__':
    #输入目标文件和日期
    target_file=sys.argv[1]

    read_directory='C:/1/test.log'
    read_directory = 'C:/1/5m'
    # target_file = 'C:/1/target_file'
    files=[]
    for root, dirs, files in os.walk(read_directory):
        pass
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
    while 1:
        for file in files:
            convert(root+'/'+file,target_file,today="",match_now_time=True)

        time.sleep(60)







