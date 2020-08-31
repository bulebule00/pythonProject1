#!/usr/bin/python3
# coding:utf-8

import datetime
import os
import re
import time

today=time.strftime("%Y-%m-%d", time.localtime())

#转换时间戳
def convert_stamp(timeStamp):
    timeArray = time.localtime(int(timeStamp))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    today=time.strftime("%Y-%m-%d", time.localtime())
    otherStyleTime=today+otherStyleTime[10:]
    timeArray = time.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return str(timeStamp)

def convert(filename,new_file):
    f1 = open(filename, mode='r', encoding='utf-8')
    f2 = open(new_file, mode='w', encoding='utf-8')
    for line in f1:
        # print('before:',line)
        date_all = re.findall(r"(\"\d{4}-\d{1,2}-\d{1,2})", line)
        for item in date_all:
            line = line.replace(item[1:], today)
        date_all = re.findall(r"(\"\d{2}-\d{1,2}-\d{1,2})", line)
        for item in date_all:
            line = line.replace(item[1:], today[2:])
            # print('after: ',line)

        #匹配_ts字段
        date_all = re.findall(r"(_ts\"\:\d{10})", line)
        for item in date_all:
            new_stamp=convert_stamp(item[5:])
            line = line.replace(item[5:], new_stamp)
            # print('after: ',line)

        f2.write(line)
        f2.flush()
    f1.close()
    f2.close()



import  sys
def main():
    for new_file in sys.argv[1:]:
        convert('2020-08-17-13-45',new_file)


if __name__ == "__main__":
    main()