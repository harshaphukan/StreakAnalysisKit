import cv2
import h5py
import MisfitLaueImage
from PIL import Image
import numpy as np

fComp=h5py.File('Hline1_5734_47.h5','r')
KComp=fComp['entry1/data']
dsetComp=KComp['data']

Array=dsetComp[...]
Array[Array<90]=1 #Scale Intensity values to accentuate the streaks
fComp.close()
print(Array)

LineList,Image=MisfitLaueImage.HoughInputArray(Array,100)
print(Image)
cv2.imwrite('Hline_5734_47H100.png',Image)
