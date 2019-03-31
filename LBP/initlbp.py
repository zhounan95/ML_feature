from extractFeature import extractFeature as EF
import numpy as np
import kCrossValidation as KCV
import os
def initLBP():
    dirPath = '/home/zhounan/Documents/ML_Feature/dataset/datasetAll'
    allData, allCountArr, label = EF(dirPath)
    print np.sum(allData[0][:])
    allLabel = getAllLabel(label, allCountArr)
    print 'allCountArr is ', allCountArr
    print 'allCountArr len is ', len(allCountArr)
    print 'allCountArr is ', np.sum(allCountArr)
    KCV.kCrossValidation(allData, allLabel, label, countArr=allCountArr)

def getAllLabel(label, allCountArr):
    result = []
    for i in range(np.shape(label)[0]):
        curNum = allCountArr[i]
        for j in range(curNum):
            result.append(label[i])
    # result = np.array(result)
    print 'label type is:', type(result)
    return result

initLBP()
