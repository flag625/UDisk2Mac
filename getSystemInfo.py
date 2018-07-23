#!/usr/bin/env python
# _-*- coding: utf-8 -*-

import psutil
import time
import logging.config

"""
   系统环境：MasOS
   获取u盘插入Mac电脑后的盘符信息
   代码参考：https://jingyan.baidu.com/article/49ad8bce91a4905834d8fa92.html
"""

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#local_device = []     #本地驱动器信息
#local_letter = []     #本地路径
#local_number = 0      #本地驱动器数

mobile_device = []    #移动设备信息
mobile_letter = []    #移动设备访问路径
mobile_number = 0     #移动设备数

#更新数据
"""
psutil.disk_partitions()，MacOS 环境的输出结果：
[
sdiskpart(device='/dev/disk1s1', 
          mountpoint='/', 
          fstype='apfs', 
          opts='rw,local,rootfs,dovolfs,journaled,multilabel'),
sdiskpart(device='/dev/disk1s4', 
          mountpoint='/private/var/vm', 
          fstype='apfs', 
          opts='rw,noexec,local,dovolfs,dontbrowse,journaled,multilabel,noatime'), 
sdiskpart(device='/dev/disk2s1', 
          mountpoint='/Volumes/FLAG625', 
          fstype='msdos', 
          opts='rw,nosuid,local,ignore-ownership')
]

利用 opts 的 "ignore-ownership" 判断disk是否为移动设备。
利用 mountpoint 获取移动设备在 Mac 上的访问路径。

"""
def updata():
    global local_device, local_letter, local_number, \
            mobile_device, mobile_letter, mobile_number

    """
    tmp_local_letter = []
    tmp_local_number = 0
    tmp_mobile_device = []
    """

    tmp_local_device = []
    tmp_mobile_letter = []
    tmp_mobile_number = 0

    try:
        disk_info = psutil.disk_partitions()
    except Exception as e:
        print("程序发生异常！！！")
        logger.info(e)
        raise e
    else:
        for part in disk_info:
            tmplist = part.opts.split(',')
            #获取移动设备信息
            if 'ignore-ownership' in tmplist:
                # 得到移动设备数量
                tmp_mobile_number += 1
                # 得到移动设备驱动器信息
                tmp_local_device.append(part)
                # 得到移动设备访问路径
                tmp_mobile_letter.append(part.mountpoint)

        mobile_device = tmp_local_device
        mobile_letter = tmp_mobile_letter
        mobile_number = tmp_mobile_number

    return mobile_number

def print_mobile_device(n):
    global local_device, local_letter, local_number, \
        mobile_device, mobile_letter, mobile_number

    print("="*50+"\n读取到"+str(n)+"个移动驱动器")
    if mobile_number:
        for i, letter in enumerate(mobile_letter):
            print("\n第 "+str(i+1)+" 个"+letter+"：{"+mobile_device[i].opts+"}")
    else:
        print("没有移动驱动器！！！")

def get_path(order):
    global mobile_letter, mobile_number
    if order > mobile_number:
        print("盘符序号超出移动磁盘数量！")
        return
    if not mobile_letter:
        print("没有移动磁盘！")
        return
    return mobile_letter[order-1]

#test
if __name__ == "__main__":
    #初次读取驱动器信息
    now_number = 0                 #实时移动设备驱动数
    before_number = updata()       #更新数据之前的驱动数
    print_mobile_device(before_number)

    #进程进入循环 Loop Seconds = 1s
    while True:
        now_number = updata()
        if(now_number > before_number):
            print("检测到移动磁盘插入...")
            print_mobile_device(now_number)
            print("请选择磁盘序号：")
            print("选择了 "+get_path(int(input())))
            before_number = now_number
        elif(now_number < before_number):
            print("检测到移动磁盘被拔出...")
            print_mobile_device(now_number)
            before_number = now_number
        time.sleep(1)



