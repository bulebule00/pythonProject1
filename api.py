#!/usr/bin/python3
# coding:utf-8

import datetime
import os
import re
import time
import  sys



#转换时间戳
def convert_stamp(timeStamp,today="",match_now_time=False):
    if today=="":
        today = time.strftime("%Y-%m-%d", time.localtime())
    timeArray = time.localtime(int(timeStamp))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    if match_now_time:
        now_time = time.strftime("%H:%M:%S", time.localtime())
        # print('3:',otherStyleTime[11:],now_time)
        if otherStyleTime[11:]!=now_time:
        # if otherStyleTime[11:][:2]!= now_time[:2]:
            # print("1")
            return timeStamp
    otherStyleTime = today + otherStyleTime[10:]
    timeArray = time.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    # print('2')
    return str(timeStamp)

def convert(filename,new_file,today="",match_now_time=False):
    if today=="":
        today = time.strftime("%Y-%m-%d", time.localtime())
    now_time = time.strftime("%H:%M:%S", time.localtime())
    f1 = open(filename, mode='r', encoding='utf-8')
    f2 = open(new_file, mode='a+', encoding='utf-8')
    for line in f1:
        date_all = re.findall(r"(\"\d{4}-\d{1,2}-\d{1,2}T\d{2}:\d{2}:\d{2})", line)
        for item in date_all:
            if match_now_time==False or (match_now_time and item[12:20] == now_time):
            # if match_now_time == False or (match_now_time and item[12:20][:2] == now_time[:2] ):
                line = line.replace(item[1:11], today)

        date_all = re.findall(r"(\"\d{2}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2})", line)
        for item in date_all:
            if match_now_time == False or (match_now_time and item[10:18] == now_time):
            # if match_now_time == False or (match_now_time and item[10:18][:2] == now_time[:2]):
                line = line.replace(item[1:9], today[2:])

        #匹配_ts字段
        date_all = re.findall(r"(_ts\"\:\d{10})", line)
        for item in date_all:
            new_stamp = convert_stamp(item[5:], today,match_now_time)
            if match_now_time == False or (match_now_time and new_stamp!=item[5:]):
                line = line.replace(item[5:], new_stamp)

        f2.write(line)
        f1.flush()
    f1.close()
    f2.close()
    print('convert:','source:',filename,'target:',new_file)

