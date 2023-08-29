
from PIL import Image
import numpy as np

for i in range(1,21):

    print("第" + str(i) + "张")
    #filename_colour = "D:\\faceNet\\faceDatasets\\Bernardo_Silva\\" + str(i) + ".jpg"  #B席
    #filename_colour = 'D:\\faceNet\\faceDatasets\\Erling_Haaland\\' + str(i) + ".png"    #哈兰德
    filename_colour = 'D:\\faceNet\\faceDatasets\\Kevin_De_Bruyne\\' + str(i) + ".png"


    def pil():
        img_colour = Image.open(filename_colour)

        image_colour = np.array(img_colour)

        # 查看修改前的size和shape
        print("-"*20 + "修改前size" + "-"*20)
        print(filename_colour + " 的size为：", img_colour.size)

        print("-"*20 + "修改前shape" + "-"*20)
        print(filename_colour + " 的shape为：", image_colour.shape)

        # 改变尺寸
        out_colour = img_colour.resize((160, 160), Image.ANTIALIAS)

        out_image_colour = np.array(out_colour)

        # 查看修改后的size和shape
        print("-" * 20 + "修改后size" + "-" * 20)
        print(filename_colour + " 的size为：", out_colour.size)

        print("-" * 20 + "修改后shape" + "-" * 20)
        print(filename_colour + " 的shape为：", out_image_colour.shape)

        # 查看通道数
        print("-"*20 + "通道数" + "-"*20)
        print(filename_colour + " 的通道数为：", len(img_colour.split()))

        # 保存
        #out_colour.save("D:\\faceNet\\faceDatasets\\Bernardo_Silva\\"+ str(i) + ".jpg")    #B席
        #out_colour.save('D:\\faceNet\\faceDatasets\\Erling_Haaland\\' + str(i) + ".png")  #哈兰德
        out_colour.save('D:\\faceNet\\faceDatasets\\Kevin_De_Bruyne\\' + str(i) + ".png")
        #out_blackWhite.save("inference/images/22.jpg")


    pil()