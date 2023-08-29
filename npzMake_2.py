import glob
import os
import cv2
import numpy as np
import random
import tensorflow as tf
from tensorflow import keras

tf.random.set_seed(520)
np.random.seed(520)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
assert tf.__version__.startswith('2.')


def Data_Generation():
    X_data = []
    Y_data = []
    path_data = []
    path_label = []

    # path_file=os.getcwd() #获取当前工作目录
    files = os.listdir('classification')  # 获取'pokemon'文件夹下的所有文件名

    for file in files:
        print(file)
        for path in glob.glob('classification/' + file + '/*.*'):
            if 'jpg' or 'png' or 'bmp' in path:  # 只获取jpg/png/bmp格式的图片
                path_data.append(path)

    random.shuffle(path_data)  # 打乱数据

    for paths in path_data:  #
        if '类别名1' in paths:  # 为每一类打标签
            path_label.append(0)
        elif '类别名2' in paths:
            path_label.append(1)
        elif '类别名3' in paths:
            path_label.append(2)
        elif '类别名4' in paths:
            path_label.append(3)

        img = cv2.imread(paths)  # 用opencv读图片数据
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv的图片通道是BGR，要转换成送入NN的RGB
        img = cv2.resize(img, (78, 170))  # 统一图片大小
        X_data.append(img)

    L = len(path_data)
    Y_data = path_label
    X_data = np.array(X_data, dtype=float)
    Y_data = np.array(Y_data, dtype='uint8')
    X_train = X_data[0:int(L * 0.8)]  # 将数据分为训练集 验证集和测试集 比例为 0.8:0.1:0.1
    Y_train = Y_data[0:int(L * 0.8)]
    X_valid = X_data[int(L * 0.8):int(L * 0.9)]
    Y_valid = Y_data[int(L * 0.8):int(L * 0.9)]
    X_test = X_data[int(L * 0.9):]
    Y_test = Y_data[int(L * 0.9):]
    return X_train, Y_train, X_valid, Y_valid, X_test, Y_test, L


X_train, Y_train, X_valid, Y_valid, X_test, Y_test, L = Data_Generation()
np.savez(os.path.join('classification', 'data.npz'), X_train=X_train, Y_train=Y_train, X_valid=X_valid, Y_valid=Y_valid,
         X_test=X_test, Y_test=Y_test)
# 打包成npz的压缩格式 储存在工程文件目录中，这样运行程序进行测试时就不用每次都重复生成数据，直接调用npz就好


