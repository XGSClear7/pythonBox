import os
import shutil

from tqdm import tqdm

# 文件目录
path = r'F:\MyProjects\spider_data\sopei\sopei'
# 结果存放目录
Data1 = r'F:\MyProjects\spider_data\sopei\高清图'
Data2 = r'F:\MyProjects\spider_data\sopei\缩略图'
# 读取文件列表
files_list = os.listdir(path)

for file in tqdm(files_list):
    filename, suffix = os.path.splitext(file)  # filename是文件名 suffix是文件后缀
    if '&type=thumbnail' not in filename:  # 判断条件
        file_path = os.path.join(path, filename + suffix)  # 文件路径
        shutil.copy(file_path, Data1)
    else:
        file_path = os.path.join(path, filename.replace('&type=thumbnail', '') + suffix)  # 文件路径
        shutil.copy(file_path, Data2)
