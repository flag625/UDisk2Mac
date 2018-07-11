#!urs/bin/env python
# _-*- coding: utf-8 -*-

import os
import shutil

"""
   系统环境：MasOS
   将移动磁盘的文件夹连同文件复制到目标地址
"""

Udisk_path  = ''     #u盘地址，U盘插入Mac后的访问地址,绝对路径
target_path = ''     #目标地址，要复制到的地址,暂定为不存在的地址，绝对路径


#复制文件，主程序
def copyFiles(s_path, t_path):
    if os.path.exists(s_path):
        if not os.path.exists(t_path):
            try:
                #目标地址不存在
                shutil.copytree(s_path, t_path)
            except Exception as e:
                raise e
        else:
            #目标地址存在
            try:
                copyfile(s_path, t_path)
            except Exception as e:
                raise e
    else:
        raise OSError

#目标地址存在
def copyfile(s_path, t_path):
    if os.path.isfile(s_path):
        shutil.copy(s_path, t_path)

    if os.path.isdir(s_path):
        s_pathlist = os.listdir(s_path)
        for inner in s_pathlist:
            s_inpath = os.path.join(s_path, inner)
            t_inpath = os.path.join(t_path, inner)
            try:
                copyFiles(s_inpath, t_inpath)
            except Exception as e:
                raise e

#test
if __name__ == "__main__":
    Udisk_path = '/Users/cloudin/Documents/test1'
    target_path = '/Users/cloudin/Documents/test3'
    print("复制文件夹：")
    copyFiles(Udisk_path, target_path)