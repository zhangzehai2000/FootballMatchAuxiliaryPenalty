from faceCore import process, predict

import cv2


def c_main(path, model, ext):
    image_data = process.pre_process(path)
    image_info= predict.predict(image_data, model, ext)


    x = image_data[0].replace('\\', '/')
    x = cv2.imread(x)


    return image_data[1] + '.' + ext, image_info


if __name__ == '__main__':
    pass
