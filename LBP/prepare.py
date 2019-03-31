# -*- coding: utf-8 -*-
import os
import SimpleITK as itk
import shutil
import prepare
import readFile

# 读取文件序列
def read_dicom_series(dir_name):
    reader = itk.ImageSeriesReader()
    dicom_series = reader.GetGDCMSeriesFileNames(dir_name)
    reader.SetFileNames(dicom_series)
    images = reader.Execute()
    image_array = itk.GetArrayFromImage(images)
    return image_array

# 保存mhd文件
def save_mhd_image(image, file_name):
    header = itk.GetImageFromArray(image)
    itk.WriteImage(header, file_name)


# 将DICOM序列转化成MHD文件
def convert_dicomseries2mhd(dicom_series_dir, newDir, file_name):
    data = read_dicom_series(dicom_series_dir)
    save_mhd_image(data, file_name)
    shutil.move('./' + file_name, newDir)


# SeriesDir = '/home/zhounan/Documents/dataset/MedicalImage/CYST/001-1132414/ART'
# file_name = 'ART.mhd'
# convert_dicomseries2mhd(SeriesDir,  file_name)


# dirPath = '/home/zhounan/Documents/ML_Feature/dataset/datasetAll'
# dirs = os.listdir(dirPath)
# for singleDir in dirs:
#     newDir = dirPath + '/' + singleDir + '/PV/Liver'
#     SeriesDir = dirPath + '/' + singleDir + '/PV/image'
#     file_name = singleDir + '_PV.mhd'
#     convert_dicomseries2mhd(SeriesDir, newDir, file_name)



# dir = '/home/zhounan/Documents/ML_Feature/dataset/datasetAll'
# dirs = os.listdir(dir)
# for singleDir in dirs:
#     roi_name = 'Tumor_' + singleDir + '_PV.mhd'
#     roi_name1 = 'Tumor_' + singleDir + '_PV.raw'
#     newDir = os.path.join(dir, singleDir, 'PV', 'Tumor_new')
#     os.makedirs(newDir)
#     imagedir = os.path.join(dir, singleDir, 'PV', 'Liver', singleDir + '_PV.mhd')
#     maskdir = os.path.join(dir, singleDir, 'PV', 'mask', 'TumorMask_' + singleDir + '_PV_01.mhd')
#     image = readFile.readSingleFile(imagedir)
#     mask = readFile.readSingleFile(maskdir)
#     print singleDir
#     roi = image * mask
#     prepare.save_mhd_image(roi, roi_name)
#     shutil.move('./' + roi_name, newDir)
#     shutil.move('./' + roi_name1, newDir)