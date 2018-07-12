# UDisk2Mac
将U盘内容拷贝到Mac电脑。
main.py :主程序。
filesCopy.py ：文件夹及文件复制子程序。
getSystemInfo.py ：获取u盘插入后的访问路径。


在终端执行main.py程序，
待系统识别到移动设备插入后，
可输入目标保存地址（根目录，如'/Users/cloudin/Documents'），
判断地址是否合法，
合法就执行复制任务。