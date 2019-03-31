# -*- coding: utf-8 -*-
import numpy as np
np.set_printoptions(threshold=np.inf)
from SimpleITK import SimpleITK as itk
# import numpy as np
# a = np.arange(6).reshape(2, 3)
# print(a)
# print('\n')
# b = sum(a)
# print(b)

'''生成肝实质mhd文件'''
# import os
# dirPath = '/home/zhounan/Documents/dataset/MedicalImage'
# dirs = os.listdir(dirPath)
# for singleDir in dirs:
#     print singleDir

# import shutil
# import os
#
# dirPath = '/home/zhounan/Documents/ML_Feature/dataset/datasetAll'
# dirs = os.listdir(dirPath)
# for singleDir in dirs:
#     newDir = os.path.join(dirPath, singleDir, 'PV', 'Liver')
#     file_name = singleDir + '_PV.raw'
#     test = os.path.join(dirPath, singleDir, 'Tumor_New', 'Tumor_' + singleDir + "_ART_1.mhd")
#     print newDir
    # shutil.move('/home/zhounan/Documents/ML_Feature/LBP (2)/' + file_name, newDir)


'''生成肝实质病灶ROI'''
import cv2
# import readFile
# import prepare
# roi_name = 'roi.mhd'
# img = readFile.readSingleFile('../dataset/datasetAll/Srr000/PV/Liver/Srr000_PV.mhd')
# mask = readFile.readSingleFile('../dataset/datasetAll/Srr000/PV/mask/TumorMask_Srr000_PV_01.mhd')
# roi = img * mask
#
# prepare.save_mhd_image(roi, roi_name)

# import readFile
#
# a = readFile.readSingleFile('/home/zhounan/Documents/ML_Feature/dataset/datasetAll/Srr016/PV/Tumor_new/Tumor_Srr016_PV.mhd')
# print a.shape
# index = np.where(a != 0)
# print index


'''计算LBP及直方图'''
# import readFile
# from skimage.feature import local_binary_pattern
# import matplotlib.pyplot as plt
#
#
# def calculatehistogram(image, eps=1e-7):
#     radius = 3
#     points = 3*8
#     lbp = local_binary_pattern(image, points, radius, method="uniform")
#     print lbp
#     n_bins = int(lbp.max() + 1)
#     (histogram, _) = np.histogram(lbp.ravel(), bins=n_bins, range=(0, n_bins))
#     print histogram
#     # now we need to normalise the histogram so that the total sum=1
#     histogram = histogram.astype("float")
#     histogram /= (histogram.sum() + eps)
#     return histogram
#
# imagefile = '/home/zhounan/Documents/ML_Feature/dataset/datasetAll/Srr000/PV/Tumor_new/Tumor_Srr000_PV.mhd'
# image = readFile.readSingleFile(imagefile)
# roi = readFile.caluROI(image)
# print roi[3, :, :].shape
# res = calculatehistogram(roi[3, :, :])
# # for i in res:
# #     for j in i:
# #         print j
# print np.sum(res)
# print res

'''读取txt文件label'''
dir = '/home/zhounan/Documents/ML_Feature/dataset/datasetAll/Srr101/label.txt'
fr = open(dir, 'r+')
dic = eval(fr.read())   #读取的str转换为字典
print dic['tumorType']
fr.close()