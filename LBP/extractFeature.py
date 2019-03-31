# -*- coding: utf-8 -*-
import os
import readFile
import numpy as np
import caluLBP as lbp
def extractFeature(dirPath):
    dirs = os.listdir(dirPath)
    dirs.sort(key=lambda x: int(x[-3:]))
    allData = []
    allCountArr = []
    labels = []
    for singleDir in dirs:
        # if singleDir.startswith('.'):
        #     continue
        pvFileName = os.path.join(dirPath, singleDir, 'PV', 'Tumor_new', 'Tumor_'+singleDir+"_PV.mhd")
        pvImages = readFile.readSingleFile(pvFileName)
        pvImagesROI = readFile.caluROI(pvImages)
        feature = lbp.caluLBP(pvImagesROI)
        #for x in range(len(feature)):
        #    allData.append(feature[x])
        allData.extend(feature)
        allCountArr.append(np.shape(feature)[0])
        print 'feature size is ', np.shape(feature)
        dir = os.path.join(dirPath, singleDir, 'label.txt')
        fr = open(dir, 'r+')
        dic = eval(fr.read())   # 读取的str转换为字典
        label = dic['tumorType']
        fr.close()
        labels.append(label)
    print 'allData size is ', np.shape(allData)
    allData = np.squeeze(allData)
    return allData, allCountArr, labels

def imageRegistration(images1,images2):
    [z0,y0,x0] = np.shape(images1)
    [z1,y1,x1] = np.shape(images2)

