# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# TODO 算法描述_dsfsdf_v2 # Kenny@20211029 
# 历遍本地Movies的路径，将所有文件都格式化成"/Movies/13(2010).1080p.BluRay.x264.DTS-HDChina/13.2010.1080p.BluRay.x264.DTS-HDChina.mkv"这样的格式
# 并获取所有文件的大小，存入字典 dLocalMovies
# 读取日志文件"Exp_Mov.txt", 将云端的Movies文件名/文件大小一个存入字典 dCloudMovies
# 对这两个字典比较，，，
#   1. 取出文件名交集后，但是文件大小不同的子集   ...  dDifFileSize
#   2. 取出本地有，远程没的子集   ...  dLocalMore
#   3. 取出本地无，远程有的子集   ...  dCloudMore

import json

# dic = {
#     "/Movies/127.Hours.2010.1080p.BluRay.x264.DTS-HDChina/127.Hours.2010.1080p.BluRay.x264.DTS-HDChina.mkv": 8535532107,
#     "/Movies/13(2010).1080p.BluRay.x264.DTS-HDChina/13.2010.1080p.BluRay.x264.DTS-HDChina.mkv": 8527274343}
# if "/Movies/127.Hours.2010.1080p.BluRay.x264.DTS-HDChina/127.Hours.2010.1080p.BluRay.x264.DTS-HDChina.mkv" in dic:
#     print(dic["/Movies/127.Hours.2010.1080p.BluRay.x264.DTS-HDChina/127.Hours.2010.1080p.BluRay.x264.DTS-HDChina.mkv"])
# if "/Movies/13(2010).1080p.BluRay.x264.DTS-HDChina/13.2010.1080p.BluRay.x264.DTS-HDChina.mkv" in dic:
#     print(dic["/Movies/13(2010).1080p.BluRay.x264.DTS-HDChina/13.2010.1080p.BluRay.x264.DTS-HDChina.mkv"])


def txt_read(files):
    txt_dict = {}
    fopen = open(files)
    i = 0
    for line in fopen.readlines():
        # line = str(line).replace("\n","") #注意，必须是双引号，找了大半个小时，发现是这个问题。
        arr = line.split(',"')
        key = arr[2][7:-1]
        if "\\u0026" in key:
            key = key.replace("\\u0026", "&")
            # print(key)
        #     i = i+1

        file_size = int(arr[1][6:])
        txt_dict[key] = file_size
        # split（）函数用法，逗号前面是以什么来分割，后面是分割成n+1个部分，且以数组形式从0开始
        # 初学python，感觉这样表达会理解一点。。
    # print(i)
    fopen.close()
    return txt_dict


dCloudMovies = txt_read('Exp_Mov.txt')
# print(dCloudMovies[
#           "/Movies/Broken.City.2013.1080p.BluRay.x264.DTS-WiKi/Broken.City.2013.1080p.BluRay.x264.DTS-WiKi.mkv"])

# 初始目录，待处理的目录，可以修改
# baseDir = "/Volumes/ELE18T-VIDEOS/^ELE18T/Animation/PiXAR.SHORT"

# dLocalMovies = walk_folder_dic("/Volumes/ELE18T-VIDEOS/^ELE18T/Movies/[一级戒备].The.Sentinel.2006")
dLocalMovies = json.load(open('./dLocalMovies.json', 'r'))
# print(dLocalMovies[
#           "/Movies/Broken.City.2013.1080p.BluRay.x264.DTS-WiKi/Broken.City.2013.1080p.BluRay.x264.DTS-WiKi.mkv"])

#   1. 取出文件名交集后，但是文件大小不同的子集   ...  dDifFileSize
# for item in dLocalMovies:
#     if item in dCloudMovies:
#         if dLocalMovies[item] != dCloudMovies[item]:
#             print(item)
#
# for item2 in dCloudMovies:
#     if item2 in dLocalMovies:
#         if dLocalMovies[item2] != dCloudMovies[item2]:
#             print(item2)

#   2. 查找本地无，远程有的子集   ...  dCloudMore 这个要从云端删掉。。。
# for item in dCloudMovies:
#     if item not in dLocalMovies:
#         print(item)

#   3. 查找本地有，远程没的子集   ...  dLocalMore  这些是新增的，需要上传
dCloudMovies, dLocalMovies
for item in dLocalMovies:
    if item not in dCloudMovies:        
        print(item)
