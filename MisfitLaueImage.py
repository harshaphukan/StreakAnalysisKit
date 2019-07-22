#!/usr/bin/env python

import h5py
import numpy as np
from PIL import Image
import cv2
from scipy import linalg as La

def LaueAdd(hdf1,hdf2):
    """Function to calculate scaled resultant intensity from two Image files corresponding
       to two adjacent Voxels as input
       Output is scaled resultant intensity array of shape 2048 x 2048 """
    FileList=[hdf1,hdf2]
    Sum=np.zeros((2048,2048))
    for i in FileList:
        f=h5py.File(i,'r')
        K=f['entry1/data']
        data=np.asarray(K['data'])
        Sum=Sum+data
        f.close()
    
    #Scale Intensity of each pixel by the minimum intensity value
    Sum=Sum/Sum.min()
    return Sum

def ImageGenerator(Array,FName):
    """ Function to generate  8-bit, single-channel binary source image, 
        given an input array"""
    LaueImage=Image.fromarray((Array*255).astype(np.uint8))
    LaueImage.save(FName)


def HoughLineImage(InputImage,T):
    """Function to generate lines connecting detected edges using Hough transform for a given image and
       specified threshold.
       Returns the pixel (X,Y) coordinates of the found lines """
    # Read image 
    InImage = cv2.imread(InputImage, cv2.IMREAD_COLOR)
    # Convert the image to gray-scale
    grayscale = cv2.cvtColor(InImage, cv2.COLOR_BGR2GRAY)
    # Find the edges in the image using canny detector
    edges = cv2.Canny(grayscale, 50, 200)
    # Detect points that form a line
    lines = cv2.HoughLinesP(edges, 1, np.pi/180,T,minLineLength=10, maxLineGap=250)
    # Draw lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(InImage, (x1, y1), (x2, y2), (255, 0, 0), 3)
    # Save Image File
    OutString=InputImage.split('.')
    OutFileName=OutString[0]+'_'+'HoughLines'+'_'+'T'+str(T)+'.png'
    cv2.imwrite(OutFileName, InImage)
    #return Line Coordinates [(x1,y1),(x2,y2)]
    LineList=[[(i[0][0],i[0][1]),(i[0][2],i[0][3])] for i in lines]
    return LineList
 

def HoughInputArray(Array,TList):
    """ Function to generate lines connecting detected edges using Hough transform for a given image array and
       specified threshold.
       Returns the pixel (X,Y) coordinates of the found lines"""
    # Read image 
    InImage=(Array*255).astype(np.uint8)
    # Find the edges in the image using canny detector
    edges = cv2.Canny(InImage, 50, 200)
    # Detect points that form a line
    lines=None
    counter=0
    while lines is None:
        lines = cv2.HoughLinesP(edges, 1, np.pi/180,TList[counter],\
                                minLineLength=10, maxLineGap=250)
        counter+=1
    # Draw lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(InImage, (x1, y1), (x2, y2), (0, 0, 255), 3)
    #Write Output Image File
    #OutFile=OutString+'HoughLines'+'T'+str(T)+'.png'
    #cv2.imwrite(OutFile, InImage)
    #return Line Coordinates [(x1,y1),(x2,y2)]
    LineList=[[(i[0][0],i[0][1]),(i[0][2],i[0][3])] for i in lines]
    return LineList,InImage,TList[counter]
    




def main():
    pass
if __name__ =="__main__":
    main()
    
