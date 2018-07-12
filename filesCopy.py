#!urs/bin/env python
# _-*- coding: utf-8 -*-

import os
import os.path
import shutil

"""
   系统环境：MasOS
   将移动磁盘的文件夹连同文件复制到目标地址
"""

Udisk_path  = ''     #u盘地址，U盘插入Mac后的访问地址,绝对路径
target_path = ''     #目标地址，要复制到的地址,暂定为不存在的地址，绝对路径


#文件夹复制，主程序
def copyFiles(s_path, t_path):
    if os.path.exists(s_path):
        if not os.path.exists(t_path):
            # 目标地址不存在
            try:
                #复制，创建新的文件目录
                print("\n创建新文件夹：" + os.path.basename(t_path) +
                      "，复制 U盘：" + os.path.basename(s_path) + "下所有文件。")
                shutil.copytree(s_path, t_path)
                print("\n******复制成功******")

            except Exception as e:
                raise e
        else:
            #目标地址存在
            try:
                print("\n*文件夹 "+os.path.basename(t_path)+" 存在，进入内部：")
                copyfile(s_path, t_path)
            except Exception as e:
                raise e
    else:
        raise OSError

#目标地址存在
def copyfile(s_path, t_path):
    if os.path.isfile(s_path):
        #t_path存在时，拷贝覆盖。
        print("\n文件 " + os.path.basename(t_path) + " 存在，更新覆盖")
        shutil.copyfile(s_path, t_path)

    if os.path.isdir(s_path):
        s_pathlist = os.listdir(s_path)
        #下一层目录
        for inner in s_pathlist:
            s_inpath = os.path.join(s_path, inner)  #下级目录
            t_inpath = os.path.join(t_path, inner)  #下级目录
            if os.path.isdir(s_inpath):
                try:
                    print("\n//有 "+inner+" 文件夹，执行复制 :")
                    copyFiles(s_inpath, t_inpath)
                except Exception as e:
                    raise e
            elif os.path.isfile(s_inpath):
                if not os.path.exists(t_inpath):
                    try:
                        print("\n创建新文件 "+inner+" ,复制")
                        shutil.copy(s_inpath, t_inpath)
                    except Exception as e:
                        raise e
                else:
                    try:
                        print("\n文件 " + inner + " 存在，更新覆盖")
                        shutil.copyfile(s_inpath, t_inpath)
                    except Exception as e:
                        raise e


#test
if __name__ == "__main__":
    Udisk_path = '/Users/cloudin/Documents/test1'
    target_path = '/Users/cloudin/Documents/test3'
    print('\n*****'+"复制： "+'*****')
    copyFiles(Udisk_path, target_path)
