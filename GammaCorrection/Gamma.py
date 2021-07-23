import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import random


# gamma correction 
def gamma_correction(img, c=1, g=2.2):
    out = img.copy() 
    out /= 255
    out = (1/c * out) ** (1/g) 
    out *= 255 
    out = out.astype(np.uint8) 
    return out 
     
# Read image 
img = cv2.imread("./GammaCorrection/input.png", cv2.IMREAD_COLOR).astype(np.float64)
# Gammma correction
count = 0 
for i in range(4):
    rand = random.randrange(80, 200)/100
    print(rand)
    out = gamma_correction(img, g=rand)
    cv2.imwrite("./GammaCorrection/out" + str(count) + ".png", out)
    count = count + 1