# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import os


def dealShitName(ShitName):
    while '  ' in ShitName:  # Python 太TM简洁了啊，，，这段简直优雅得不行了
        ShitName = ShitName.replace('  ', ' ')
    while '..' in ShitName:
        ShitName = ShitName.replace('..', '.')
    GoodName = ShitName.replace(' ', '.').replace('\'', ',')  # '这个符号用半角逗号替代,因为SB的189网盘缺陷...
    GoodName = GoodName.replace('.-.', '.').replace(',.', ',')  # 局部额外做一些操作？

    return GoodName


# rename file name 的代码段
# old_file_name = "./Don't    Cool     Sample.srt"
# old_file_name = "./Kenny's  B  Cool       Sample.srt"
#
# print(old_file_name)
# print(dealShitName(old_file_name))
# print(os.path.isfile(old_file_name))

def isShitName(sIN):
    ShitPatterns = [' ','..', '\'', '.-.', ',.']    # 其实 $ & 这两个字符也会戳到189的盘，，，导致它傻逼...太蠢了...
    for ShitPattern in ShitPatterns:
        if ShitPattern in sIN:
            return True
    return False
    # return any([' ' in sIN, '\'' in sIN, '.-.' in sIN, '..' in sIN, ',.' in sIN])  # 说是更优雅的写法，但是其实并没觉得有多优雅.
    # return ' ' in sIN or '\'' in sIN or '.-.' in sIN or '..' in sIN or ',.' in sIN


# 初始目录，待处理的目录，可以修改
baseDir = "/Volumes/ELE18T-VIDEOS/^ELE18T/Animation"

# 这里walk 的第二个参数设置为False很重要，topdown=True,默认值是真，表示从根目录到子目录历遍，这里要从最子目录开始历遍，所以要设置为False
for dirpath, dirnames, filenames in os.walk(baseDir, False):
    for filename in filenames:
        if isShitName(filename):
            old_file_name = os.path.join(dirpath, filename)
            new_file_name = os.path.join(dirpath, dealShitName(filename))
            # print(old_file_name)
            os.rename(old_file_name, new_file_name)
            # os.rename
            print(new_file_name)
    for dirname in dirnames:
        if isShitName(dirname):
            old_dir_name = os.path.join(dirpath, dirname)
            new_dir_name = os.path.join(dirpath, dealShitName(dirname))
            # print(old_dir_name)
            os.rename(old_dir_name, new_dir_name)
            print(new_dir_name)
# for dirpath, dirnames, filenames in os.walk('.'):


# new_file_name = "./testLog.log2"
# os.rename(old_file_name, new_file_name)
# print("File renamed!")
