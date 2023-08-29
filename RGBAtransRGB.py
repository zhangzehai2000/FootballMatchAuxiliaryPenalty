from PIL import Image
import os
import string
from matplotlib import pyplot as plt

#path = 'D:\\faceNet\\faceDatasets\\Erling_Haaland\\'  # 最后要加双斜杠，不然会报错
path = 'D:\\faceNet\\faceDatasets\\Kevin_De_Bruyne\\'
filelist = os.listdir(path)

for file in filelist:
    whole_path = os.path.join(path, file)
    img = Image.open(whole_path)  # 打开图片img = Image.open(dir)#打开图片
    img = img.convert("RGB")  # 将一个4通道转化为rgb三通道
    #save_path = 'D:\\faceNet\\faceDatasets\\Erling_Haaland\\'
    save_path = 'D:\\faceNet\\faceDatasets\\Kevin_De_Bruyne\\'
    # img.save(save_path + img1)
    img.save(save_path + file)