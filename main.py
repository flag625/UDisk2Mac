#!urs/bin/env python
# _-*- coding: utf-8 -*-

import psutil
import time
import logging.config
import os
import shutil

from UDisk2Mac import getSystemInfo as ginfo
from UDisk2Mac import filesCopy as copy

def setup():
    return input('''
    输入您的目标地址（绝对路径）：
    ''')

def main():

    copy.target_path = setup()

    before_number = ginfo.updata()  # 执行前移动设备驱动数
    ginfo.print_mobile_device(before_number)

    # 进程进入循环 Loop Seconds = 1s
    while True:
        now_number = ginfo.updata()
        s_pathlist = ginfo.mobile_letter
        if (now_number > before_number):
            print("检测到移动磁盘插入...")
            ginfo.print_mobile_device(now_number)
            before_number = now_number
            for i in range(0,now_number):
                try:
                    copy.Udisk_path = s_pathlist[i]
                    copy.copyFiles()
                except Exception as e:
                    raise e
        elif (now_number < before_number):
            print("检测到移动磁盘被拔出...")
            ginfo.print_mobile_device(now_number)
            before_number = now_number
        time.sleep(1)


if __name__ == "__main__":
    main()