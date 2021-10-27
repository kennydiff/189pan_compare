import os
import json

# 将所有的本地 mov的目录导出到字典并持久化到文件 ,否则在debug的时候每次要历遍本地的上万文件，效率很低并且很损耗磁盘。

def walk_folder_dic(folder):
    file_dict = {}
    # 这里walk 的第二个参数设置为False很重要，topdown=True,默认值是真，表示从根目录到子目录历遍，这里要从最子目录开始历遍，所以要设置为False
    for dirpath, dirnames, filenames in os.walk(folder, False):
        for filename in filenames:
            # if isShitName(filename):
            old_file_name = os.path.join(dirpath, filename)
            # new_file_name = os.path.join(dirpath, dealShitName(filename))
            # print(old_file_name)
            # os.rename(old_file_name, new_file_name)
            # os.rename
            dic_file_name = old_file_name[30:]
            file_dict[dic_file_name] = os.path.getsize(old_file_name)
            # print(old_file_name[30:])  # /Volumes/ELE18T-VIDEOS/^ELE18T/Movies/[一级戒备].The.Sentinel.2006/The.Sentinel.2006.BDrip.x264.a720.AC3.w@SiLU.mkv
            # print(os.path.getsize(old_file_name))

        # for dirname in dirnames:
        #     # if isShitName(dirname):
        #         old_dir_name = os.path.join(dirpath, dirname)
        #         # new_dir_name = os.path.join(dirpath, dealShitName(dirname))
        #         # print(old_dir_name)
        #         # os.rename(old_dir_name, new_dir_name)
        #         print(old_dir_name)
    return file_dict


dLocalMovies = walk_folder_dic("/Volumes/ELE18T-VIDEOS/^ELE18T/Movies")

fp = open('./dLocalMovies.json', 'w')
json.dump(dLocalMovies, fp)
fp.close()

# x = json.load(open('./dLocalMovies.json', 'r'))
#
# s = json.dumps(dLocalMovies)
# y = json.loads(s)