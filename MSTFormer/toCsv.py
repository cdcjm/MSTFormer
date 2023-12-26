import pandas as pd

# import pickle

import torch


data = torch.load('./data/AIS2021_72_48_24_3s_test/~train.pkl')
# # 读取.pkl文件
# data = pd.read_pickle('./data/AIS2021_72_48_24_3s_test/-train.pkl')

# 将数据转换为CSV格式并保存
df = pd.DataFrame(data)
df.to_csv(r'newPATH.csv')