import cv2
import numpy as np
import matplotlib.pyplot as plt

#文件读取
img = cv2.imread('D:\\faceNet\\faceDatasets\\Kevin_De_Bruyne')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)		#转换为灰度图
label = cv2.imread('D:\\faceNet\\faceDatasets\\Kevin_De_Bruyne\\2.jpg')
labelcol_gray = cv2.cvtColor(label,cv2.COLOR_BGR2GRAY)

#图像显示
plt.xticks([]), plt.yticks([]) # 隐藏x和y轴
plt.imshow(img_gray,cmap='gray');

plt.xticks([]), plt.yticks([]) # 隐藏x和y轴
plt.imshow(labelcol_gray,cmap='gray');

#保存为npz文件
np.savez('D:\\faceNet\\faceDatasets\\faceDatasets.npz')#image = img_gray ,label = labelcol_gray

#读取npz文件
dataset = np.load('D:\\faceNet\\faceDatasets\\faceDatasets.npz')
for item in dataset.files:
    print(dataset[item])
