import numpy as np
# 加载数据
datas = np.load("D:\\faceNet\\npz\\Database.npz")

for key, arr in datas.items():
    print(key, ": ", arr)