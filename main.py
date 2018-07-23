#!/usr/bin/env python
# _-*- coding: utf-8 -*-

import psutil
import time
import logging.config
import os
import shutil

import sys
sys.path.append('/Users/cloudin/PycharmProjects/UDisk2Mac/UDisk2Mac')

from UDisk2Mac import getSystemInfo as ginfo
from UDisk2Mac import filesCopy as copy

#自定义保存路径，最多输入4次。
def setup(try_num = 3):
    t_path = input('''
    输入您的目标地址（绝对路径）：
    ''')
    if not os.path.exists(t_path):
        t_path = None
        if try_num > 0:
            print("\n无效路径！！！")
            print("\n第 "+str(3-try_num+1)+" 次重新输入")
            try_num -= 1
            t_path = setup(try_num)
    return t_path


def main():

    before_number = ginfo.updata()  # 执行前，移动设备驱动数
    ginfo.print_mobile_device(before_number)

    # 进程进入循环 Loop Seconds = 1s
    while True:
        now_number = ginfo.updata()
        #s_pathlist = ginfo.mobile_letter
        if (now_number > before_number):
            print("检测到移动磁盘插入...")
            ginfo.print_mobile_device(now_number)
            before_number = now_number
            order = int(input("请选择磁盘序号："))
            #执行复制任务
            if now_number and order:
                try:
                    #获取移动磁盘路径
                    copy.Udisk_path = ginfo.get_path(order)
                    if not copy.Udisk_path:
                        print("\n无效序号!")
                        break
                    #自定义保存路径
                    savefiles = os.path.basename(copy.Udisk_path) + '_copy'
                    savedir   = setup()
                    if not savedir:
                        print("\n无效路径!!!")
                        break
                    copy.target_path = os.path.join(savedir,savefiles)
                    copy.copyFiles(copy.Udisk_path, copy.target_path)
                    print("Copy successed!")
                except Exception as e:
                    raise e
                finally:
                    print("\nOrder "+str(order)+" Drive Copy-Operation End!")
        elif (now_number < before_number):
            print("检测到移动磁盘被拔出...")
            ginfo.print_mobile_device(now_number)
            before_number = now_number
        time.sleep(1)


if __name__ == "__main__":
    main()
    #setup()