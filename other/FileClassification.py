import os
import shutil

from tqdm import tqdm

# 文件目录
path = r'E:\spider_data\imgs'
# 结果存放目录
Data1 = r'E:\spider_data\高清图'
Data2 = r'E:\spider_data\缩略图'
# 读取文件列表
files_list = os.listdir(path)

for file in tqdm(files_list):
    filename, suffix = os.path.splitext(file)  # filename是文件名 suffix是文件后缀
    # print(filename)
    if '&type=thumbnail' not in filename:  # 判断条件
        file_path = os.path.join(path, filename + suffix)  # 文件路径
        # print(file_path)
        shutil.copy(file_path, Data1)
    else:
        file_path = os.path.join(path, filename + suffix)  # 文件路径
        # print(file_path)
        shutil.copy(file_path, Data2)
