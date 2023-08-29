import datetime
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *
from recognition.test import *
from processor.FaceYOLODetector import Face_Detector
from processor.FallYOLODetector import Fall_Detector
from processor.TeamYOLODetector import Team_Detector

import core.main
import faceCore.main
import slideTackleCore.main

UPLOAD_FOLDER = r'./uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg'])
app = Flask(__name__)
app.secret_key = 'secret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

werkzeug_logger = rel_log.getLogger('werkzeug')
werkzeug_logger.setLevel(rel_log.ERROR)

# 解决缓存刷新问题
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


# 添加header解决跨域
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


#premierLeague
@app.route('/home/premierLeague/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    #la = None
    print(datetime.datetime.now(), file.filename)
    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)
        shutil.copy(src_path, './tmp/ct')
        image_path = os.path.join('./tmp/ct', file.filename)

        #params = {"source": os.getcwd()+r"\tmp\ct"+file.filename}
        #labels = detect(setOPT(**params))
        #print('labels是' + labels)

        def setopt(**params):
            # 文件配置
            # *******************************************************

            parser = argparse.ArgumentParser()
            parser.add_argument('--weights', type=str, default="D:\\pythonLearn\\face-net\\weights\\face_last.pt",
                                help='model.pt path')
            parser.add_argument('--source', type=str, default=os.getcwd()+r"\tmp\ct\\"+file.filename,
                                help='source')  # file/folder, 0 for webcam
            parser.add_argument('--output', type=str, default='./tmp/draw',
                                help='output folder')  # output folder
            parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
            parser.add_argument('--conf-thres', type=float, default=0.3, help='object confidence threshold')
            parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
            parser.add_argument('--fourcc', type=str, default='mp4v', help='output video codec (verify ffmpeg support)')
            parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
            parser.add_argument('--view-img', action='store_true', help='display results')
            parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
            parser.add_argument('--classes', nargs='+', type=int, help='filter by class')
            parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
            parser.add_argument('--augment', action='store_true', help='augmented inference')
            parser.add_argument('--facenet-model-path', type=str,
                                default='D:\\pythonLearn\\face-net\\resouces\\20180402-114759\\20180402-114759.pb',
                                help='miss facenet-model')
            parser.add_argument('--svc-path', type=str, default='D:\\pythonLearn\\face-net\\resouces\\SVCmodel.pkl',
                                help='miss svc')
            parser.add_argument('--database-path', type=str, default='D:\\pythonLearn\\face-net\\Database.npz',
                                help='miss database')
            opt = parser.parse_args()
            opt.img_size = check_img_size(opt.img_size)
            print(opt)

            return opt

        '''
        picture_path = 'D:\\pythonLearn\\face-net\\resouces\\faceDatasets'  # 用户图片数据
        model_path = "D:\\pythonLearn\\face-net\\resouces\\20180402-114759\\20180402-114759.pb"  # facenet模型权重
        database_path = 'D:\\pythonLearn\\face-net\\Database.npz'  # 打包成npz文件
        SVCpath = "D:\\pythonLearn\\face-net\\resouces\\SVCmodel.pkl"  # 通过SVM训练保存到pkl
        weights = "D:\\pythonLearn\\face-net\\weights\\face_last.pt"
        view_img = 'store_true'
        save_txt = 'store_true'
        imgsz = 640
        output = './tmp/draw'
        source = os.getcwd()+r"\tmp\ct"+file.filename
        labels = detect(setopt())
        '''
        labels = detect(setopt())
        print('$$$')
        print(labels)
        print('$$$')
        labels = list(labels)
        #置信度
        ''''
        confidence_level_list = []
        labels_name_list = []
        for i in range(len(labels)):
            confidence_level = list(labels[i])[-4:]
            confidence_level = ''.join(confidence_level)
            labels_name = list(labels[i])[2:-7]
            labels_name = ''.join(labels_name)
            confidence_level_list.append(confidence_level)
            labels_name_list.append(labels_name)
        print(confidence_level_list)
        print(labels_name_list)


        '''
        confidence_level = labels[-4:]
        confidence_level = ''.join(confidence_level)
        print(confidence_level)
        labels_name = labels[2:-7]
        labels_name = ''.join(labels_name)
        print(labels_name)

        print("----------------------------------")

        current_app.model = Face_Detector()
        #current_app.model = detect(setOPT(**params))
        pid, image_info= faceCore.main.c_main(
            image_path, current_app.model, file.filename.rsplit('.', 1)[1])
        #print('labels是' + str(labels))
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/tmp/ct/' + pid,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
                        'image_info': image_info,
                        'labels': labels_name,
                        'confidence_level': confidence_level,
                        'labels_list': labels_name
                        })

    return jsonify({'status': 0})



#slideTackle
@app.route('/home/slideTackle/upload', methods=['GET', 'POST'])
def upload_file1():
    file = request.files['file']
    print(datetime.datetime.now(), file.filename)
    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)
        shutil.copy(src_path, './tmp/ct')
        image_path = os.path.join('./tmp/ct', file.filename)
        current_app.model = Fall_Detector()
        pid, image_info = slideTackleCore.main.c_main(
            image_path, current_app.model, file.filename.rsplit('.', 1)[1])
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/tmp/ct/' + pid,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
                        'image_info': image_info})

    return jsonify({'status': 0})


#penalize
@app.route('/home/penalize/upload', methods=['GET', 'POST'])
def upload_file2():
    file = request.files['file']
    print(datetime.datetime.now(), file.filename)
    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)
        shutil.copy(src_path, './tmp/ct')
        image_path = os.path.join('./tmp/ct', file.filename)
        current_app.model = Team_Detector()
        pid, image_info, RAPenalize, RBPenalize, LAPenalize, LBPenalize = core.main.c_main(
            image_path, current_app.model, file.filename.rsplit('.', 1)[1])
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/tmp/ct/' + pid,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
                        'image_info': image_info,
                        'RAPenalize': RAPenalize,
                        'RBPenalize': RBPenalize,
                        'LAPenalize': LAPenalize,
                        'LBPenalize': LBPenalize
                        })

    return jsonify({'status': 0})


# show photo
@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if not file is None:
            image_data = open(f'tmp/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)

