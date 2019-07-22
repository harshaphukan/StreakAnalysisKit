#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StreakAnalysisKit import MisfitLaueImage
import h5py
import numpy as np
from PIL import Image

def PatternHough(H5FileName,H5FilePath,TList):
   fComp=h5py.File(H5FilePath+H5FileName,'r')
   KComp=fComp['entry1/data']
   dsetComp=KComp['data']
   Array=np.asarray(dsetComp[...])
   Array[Array<90]=1
   fComp.close()
   #OutFileName=H5FileName.split('.')[0]+'.png'
   Im=Image.fromarray((Array*255).astype(np.uint8))
   #Im.save(OutFilePath+OutFileName)
   LineList,InImage,TFinal=MisfitLaueImage.HoughInputArray(Array,TList)
   return LineList,InImage,TFinal

def main():
   pass

if __name__=="__main__":
   main()
