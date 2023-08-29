import os

import numpy as np

file_path = 'D:\\faceNet\\faceDatasets'

filenames = os.listdir(file_path)

print(filenames)
# all_file = []


all_file = {}

for file in filenames:
    load_path = os.path.join(file_path, file)

    print(load_path)

    name = file.split('.')[0]

    print(name)

    lab_1 = filenames[0]
    lab_2 = filenames[1]
'''
    key1 = 'emb'

    key2 = 'lab'
    
    value1 = 

    value2 = ['Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 
            'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 
            'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 
            'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 
            'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 'Erling_Haaland' 
            'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 
            'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 
            'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 
            'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 
            'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' 'Kevin_De_Bruyne' ]


    all_dict = {key1: value1, key2: value2}

    all_file[f'{name}'] = all_dict  # dict的形式保存

    # all_file.append(all_dict)  list的形式保存

dataset = np.savez("D:\\faceNet\\faceDatasets\\faceDatasets.npz", filenames, all_file)

for item in dataset.files:
    print(dataset[item])

'''