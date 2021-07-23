import cv2
import random
import os
import numpy as np


path = "./Makedefect/test/B/"

defects_list = os.listdir("./Makedefect/defects/")
AnsImage = cv2.imread("./Makedefect/Ans.png", cv2.IMREAD_COLOR)

file_list = os.listdir(path)
print(file_list)
for file in file_list:
    RotAngle = random.randint(0, 359)
    RotScale = random.randint(8, 10)/10     # scale 범위 설정 (0.5 ~ 1)
    src = cv2.imread("./Makedefect/defects/" + random.choice(defects_list), cv2.IMREAD_UNCHANGED)  # 흠집 영상
    dst = cv2.imread(path + str(file), cv2.IMREAD_COLOR) # 붙는 영상
    gray = cv2.cvtColor(AnsImage, cv2.COLOR_BGR2GRAY)
    scale = 1   # 흠집 사이즈가 영상보다 큰 경우 비율 스케일링
    h = src.shape[0]
    w = src.shape[1]

    if h > 1024 or w > 1024:
       if h > w:
           scale = 1024/h
       else:
           scale = 1024/w
    print("="*10)
    print(h)
    print(w)
    H_pos = random.randint(0, 1024 - h*scale)
    W_pos = random.randint(0, 1024 - w*scale)

    
    cp = (src.shape[1]/2, src.shape[0]/2)   #회전 중심좌표
    rot = cv2.getRotationMatrix2D(cp, RotAngle, RotScale*scale) #중심좌표, 각도(반시계), 스케일
    src = cv2.warpAffine(src, rot, (0, 0))
    for i in range(int(h*scale)):
        for j in range(int(w*scale)):
            if src[i][j][3] == 255:
                dst[H_pos + i][W_pos + j] = src[i][j][:3]
                gray[H_pos + i][W_pos + j] = 255

    if not os.path.isdir("./Makedefect/test/B_d"):
        os.mkdir("./Makedefect/test/B_d")
    if not os.path.isdir("./Makedefect/test/Ans_d/"):
        os.mkdir("./Makedefect/test/Ans_d/")    

    cv2.imwrite("./Makedefect/test/B_d/" + str(file), dst)
    cv2.imwrite("./Makedefect/test/Ans_d/" + str(file), gray)
