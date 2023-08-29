import numpy as np

npz_path = 'D:\\faceNet\\faceDatasets\\faceDatasets.npz'

# words.npy lables.npy
data = np.load(npz_path, allow_pickle=True)
for item in data.files:
    print(data[item])
