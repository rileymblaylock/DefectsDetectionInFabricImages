#Riley Blaylock

import cv2
import numpy as np
import os

imageTitle = input("Enter name of one of the same images. If new image, do not expect good results, only if dark image with light colored defect.")

#get current file path for image
path = os.path.dirname(os.path.abspath(__file__))
imagejpg = os.path.join(path, imageTitle)
#read in image in grayscale
img = cv2.imread(imagejpg, 0)
cv2.imshow('image', img)
cv2.waitKey(0)
#normalize image
cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('normalized', img)
cv2.waitKey(0)
#blur image, not for 0158.jpg, comment out when running it
img = cv2.bilateralFilter(img, 5, 50, 50)
cv2.imshow('blur', img)
cv2.waitKey(0)
if(imageTitle == "0106.jpg"):
    #threshold image
    ret,img = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    #open image to reduce noise
    kernel = np.ones((3,3),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
if(imageTitle == "0003.jpg"):
    #threshold image
    ret,img = cv2.threshold(img,205,255,cv2.THRESH_BINARY)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    #open image to reduce noise
    kernel = np.ones((3,3),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
if(imageTitle == "0012.jpg"):
    #hist eq
    img = cv2.equalizeHist(img)
    cv2.imshow('eqhist', img)
    cv2.waitKey(0)
    #threshold image
    ret,img = cv2.threshold(img,140,255,cv2.THRESH_BINARY)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    #open image to reduce noise
    kernel = np.ones((3,3),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=4)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
if(imageTitle == "0020.jpg"):
    ret,img = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    #open image to reduce noise
    kernel = np.ones((2,2),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
    img = cv2.dilate(img, kernel, iterations=2)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
if(imageTitle == "0041.jpg"):
    #threshold image
    ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    #open image to reduce noise
    kernel = np.ones((2,2),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
if(imageTitle == "0076.jpg"):
    #threshold image
    ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    #open image to reduce noise
    kernel = np.ones((3,3),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
if(imageTitle == "0158.jpg"):
    #edge detection
    kernel = np.ones((2,2),np.uint8)
    erosion = cv2.erode(img,kernel,iterations = 1)
    dilation = cv2.dilate(img,kernel,iterations = 1)
    both = dilation - erosion
    img = cv2.erode(both,kernel,iterations = 1)
    cv2.imshow('edge detection with both dilation and erosion', img)
    cv2.waitKey(0)
    img = cv2.bilateralFilter(img, 5, 550, 550)
    cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite("0158norm2.jpg", img)
    ret,img = cv2.threshold(img,140,255,cv2.THRESH_BINARY)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    kernel = np.ones((2,3),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
if(imageTitle == "0192.jpg"):
    #threshold image
    ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    #open image to reduce noise
    kernel = np.ones((2,2),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
else:
    #threshold image
    ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imshow('threshold', img)
    cv2.waitKey(0)
    #open image to reduce noise
    kernel = np.ones((3,3),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imshow('3x3 opening', img)
    cv2.waitKey(0)
    cv2.imwrite("outputimage.jpg", img)