import cv2
import os
import re


p = re.compile("(\d)([.]\S+)")


path = "./ImageCrop/"
if not os.path.isdir(path + "A"):
    os.mkdir(path + "A")
if not os.path.isdir(path + "B"):
    os.mkdir(path + "B")
if not os.path.isdir(path + "Ans"):
    os.mkdir(path + "Ans") 

Src_path = "./Makedefect/test/"
Cur_path = [["A/", "A/"], ["B_check/", "B/"], ["Ans_check/", "Ans/"]]

for Cur in Cur_path:
    filelist = os.listdir(Src_path + Cur[0])
    for file in filelist:
        num = p.search(file)
        count = 0
        src = cv2.imread(Src_path + Cur[0] + file, cv2.IMREAD_COLOR)
        for i in range(4):
            for j in range(4):
                dst = src[256*i:256*(i+1), 256*j:256*(j+1)].copy()
                cv2.imwrite(path + Cur[1] + str(num.group(1)) + "_" + str(count) + ".png", dst)
                count = count + 1
