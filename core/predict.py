import cv2
from processor.FaceYOLODetector import Face_Detector

def predict(dataset, model, ext):
    global img_y
    x = dataset[0].replace('\\', '/')
    file_name = dataset[1]
    print(x) #x为文件路径
    print(file_name)
    x = cv2.imread(x)
    img_y, image_info, RAPenalize, RBPenalize, LAPenalize, LBPenalize = model.detect(x)

    #img_y = model.detect(x)[0]
    #image_info = model.detect(x)[1]



    cv2.imwrite('./tmp/draw/{}.{}'.format(file_name, ext), img_y)
    #print(image_info) #检测框上的信息，大小，置信度
    #print(img_y)#bone
    return image_info, RAPenalize, RBPenalize, LAPenalize, LBPenalize