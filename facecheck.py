import cv2
import numpy as np
global num
num = np.array([0,0,0,0])
casceade_file = "C:\\Users\\SysUser\\Documents\\Language\\Lp\\data\\haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(casceade_file)

def facenum(num):
    if num[0] != max(num[1:]) & max(num[1:]) != 0:
        num[0] = max(num[1:])
        print('{}人検出しました。'.format(num[0])) 

def rotate(angle, img, a = 1):
    global num
    h, w, c = img.shape
    mat = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    img_rot = cv2.warpAffine(img, mat, (w, h), flags=cv2.INTER_CUBIC)

    face_list = cascade.detectMultiScale(img_rot)
    color = (0, 0, 255)

    if a == 1:
        #num[0]は前回の検出人数最大 
        if angle == 30:
            num[1] = len(face_list) 
        elif angle == 60:
            num[2] == len(face_list)
        else:
            num[3] == len(face_list)
        facenum(num)
        
    if len(face_list) > 0 : 
        for face in face_list : 
            x, y, w, h = face
            cv2.rectangle(img_rot, (x,y), (x+w, y+h), color, thickness=2)
    return img_rot

