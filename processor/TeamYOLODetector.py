import torch
import numpy as np
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords, letterbox
from yolov5_utils.torch_utils import select_device
import cv2
from random import randint

from yolov5_utils.plots import Annotator, colors, save_one_box


class Team_Detector(object):

    def __init__(self):
        self.img_size = 640
        self.threshold = 0.4
        self.max_frame = 160
        self.init_model()

    def init_model(self):

        self.weights = 'weights/team_last.pt'
        self.device = '0' if torch.cuda.is_available() else 'cpu'
        self.device = select_device(self.device)
        model = attempt_load(self.weights, device=self.device)
        model.to(self.device).eval()
        model.float()
        # torch.save(model, 'test.pt')
        self.m = model
        self.names = model.module.names if hasattr(
            model, 'module') else model.names
        self.colors = [
            (randint(0, 255), randint(0, 255), randint(0, 255)) for _ in self.names
        ]

    def preprocess(self, img):

        img0 = img.copy()
        img = letterbox(img, new_shape=self.img_size)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.float()  # 半精度
        img /= 255.0  # 图像归一化
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        return img0, img

    def plot_bboxes(self, image, bboxes, line_thickness=None):
        tl = line_thickness or round(
            0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
        #for (x1, y1, x2, y2, cls_id, conf) in bboxes:
        #color=(128, 128, 128)
        #cls_id =(128, 128, 128)
        for (x1, y1, x2, y2, cls_id, conf) in bboxes:
            #color = self.colors[self.names.index(cls_id)]
            color = (128, 128, 128)
            c1, c2 = (x1, y1), (x2, y2)
            cv2.rectangle(image, c1, c2, color,
                          thickness=tl, lineType=cv2.LINE_AA)
            global L, R
            #最左端横坐标
            L = str(c1[0])
            #print("最左点的横坐标为：" + L)
            #最右端横坐标
            #R = str(c2[0])
            #print("最右点的横坐标为" + R)
            #print('左右(' + L + ',' + R + ')')
            #
            tf = max(tl - 1, 1)  # font thickness
            t_size = cv2.getTextSize(
                cls_id, 0, fontScale=tl / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
            cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
            cv2.putText(image, '{} ID-{:.2f}'.format(cls_id, conf), (c1[0], c1[1] - 2), 0, tl / 3,
                        [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        return image,


    def detect(self, im):

        im0, img = self.preprocess(im)

        pred = self.m(img, augment=False)[0]
        pred = pred.float()
        pred = non_max_suppression(pred, self.threshold, 0.3)

        pred_boxes = []
        image_info = {}
        LEFT = []
        RIGHT = []
        count = 0
        for det in pred:
            if det is not None and len(det):
                det[:, :4] = scale_coords(
                    img.shape[2:], det[:, :4], im0.shape).round()

                for *x, conf, cls_id in det:
                    lbl = self.names[int(cls_id)]
                    #lbl = self.names[int(cls_id)] + 'L' + L + 'R' + R
                    x1, y1 = int(x[0]), int(x[1])#左端横纵
                    x2, y2 = int(x[2]), int(x[3])#右端横纵
                    pred_boxes.append(
                        (x1, y1, x2, y2, lbl, conf))
                    LEFT.append((x1,  lbl))
                    RIGHT.append((x2, lbl))
                    count += 1
                    key = '{}-{:02}'.format(lbl, count)
                    #key = '{}-{:02}'.format(lbl, )
                    image_info[key] = ['{}×{}'.format(
                        x2-x1, y2-y1), np.round(float(conf), 3)]


        #TeamLEFT
        i = 0
        TAL = []#A队左端坐标列表
        TBL = []
        for i in range(len(LEFT)):
            if LEFT[i][1] == 'TeamA':
                TAL.append(LEFT[i][0])
                i += 1
            else:
                TBL.append(LEFT[i][0])
                i += 1
        TAL = sorted(TAL, reverse=True)
        TBL = sorted(TBL, reverse=True)
        #Team
        a = 0
        TAR = []
        TBR = []
        for a in range(len(RIGHT)):
            if RIGHT[a][1] == 'TeamA':
                TAR.append(RIGHT[a][0])
                a += 1
            else:
                TBR.append(RIGHT[a][0])
                a += 1
        TAR = sorted(TAR, reverse=True)
        TBR = sorted(TBR, reverse=True)
        #Penalize
        #向右进攻
        #A队防守
        if TAR[0] > TBR[0]:
            RAPenalize = '不越位'
        else:
            RAPenalize = '越位'
        #B队防守
        if TBR[0] > TAR[0]:
            RBPenalize = '不越位'
        else:
            RBPenalize = '越位'
        #向左进攻
        #A队防守
        if TAL[0] < TBL[0]:
            LAPenalize = '不越位'
        else:
            LAPenalize = '越位'
        #B队防守
        if TBL[0] < TAL[0]:
            LBPenalize = '不越位'
        else:
            LBPenalize = '越位'


        #print(pred_boxes)
        #LEFT = self.plot_bboxes(im, pred_boxes)[1]
        #RIGHT = self.plot_bboxes(im, pred_boxes)[2]
        im = self.plot_bboxes(im, pred_boxes)[0]
        #return im, image_info, LEFT, RIGHT
        return im, image_info, RAPenalize, RBPenalize, LAPenalize, LBPenalize
