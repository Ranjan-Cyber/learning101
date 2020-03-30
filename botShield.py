import cv2
import numpy as np 
import matplotlib.pyplot as plt 
if __name__=='__main__':
    im=cv2.imread("robot.jpg")
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(im, contours, -1, (0,255,0), 3)
    cv2.imshow("Contour image",im)
    cv2.waitKey(50000)
