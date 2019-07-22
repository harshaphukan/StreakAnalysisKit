#!/usr/bin/env python
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import PatternHough


def mse(imageA, imageB):
    """the 'Mean Squared Error' between the two images is the
       sum of the squared difference between the two images;
      NOTE: the two images must have the same dimension"""
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
 
def compare_images(h5R,h5N,H5FilePath,ThresholdList):
    """compute the mean squared error and structural similarity
       index for the images. Streak files are in hdf5 format"""
    #h5R: Streak File corresponding to reference voxel
    #h5N: Streak File corresponding to Neighboring Voxel
    #H5FilePath:Location of streak files
    #ThresholdList: List of threshold values in descending order for Hough Transform
    #The threshold values are iteratively changed until an non empty Image array is obtained!
    
    #Read the hdf5 image files!!!
    #Perform Hough Transforms to identify commonalities in Streak Images
    _,InImageR,TFR=PatternHough.PatternHough(h5R,H5FilePath,\
                                               ThresholdList) 
    _,InImageN,TFN=PatternHough.PatternHough(h5N,H5FilePath,\
                                               ThresholdList) 
    
    m = mse(InImageR, InImageN) #Compute Mean square error between the two images
    s = ssim(InImageR, InImageN) #Compute SSIM
    
    return m,s,TFR,TFN
    

    
    
def main():
    pass


if __name__=="__main__":
    main()
    
