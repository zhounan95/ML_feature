# -*- coding: utf-8 -*-
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
def myKNN(data, label, testData, testLabel, testTrueLabel, countArr):
    '''
        testlabel是每张slice的label，testTrueLabel是每个case的label（一组slices）data是train数据，label是train的标签
    '''
    accuracy = []
    trueAccuracy = []
    for i in range(9):
        print np.shape(data)
        print np.shape(testLabel)
        print np.shape(testTrueLabel)
        model = KNeighborsClassifier(n_neighbors=(i+1))
        model.fit(data, label)
        predictRes = model.predict(testData)
        accuracy.append(metrics.accuracy_score(testLabel, predictRes))  #每个slice结果准确率
        index = 0
        errorCount = 0
        for i in range(len(countArr)):
            classifyMapping = [0, 0, 0, 0, 0]
            for j in range(countArr[i]):
                # print 'index is ',index
                classifyMapping[int(predictRes[index])-1] += 1
                index += 1
            indexs = getMaxIndexs(classifyMapping)
            flag = False
            for z in indexs:
                if z == testTrueLabel[i]:
                    flag = True
                    break
            if flag == False:
                errorCount += 1
        trueAccuracy.append(1-((errorCount*1.0)/(len(countArr)*1.0)))  # 经过投票之后的结果的准确率 对一个case
        print 'accuracy is ', accuracy
        print 'trueAccuracy is ', trueAccuracy
    return accuracy, trueAccuracy
def getMaxIndexs(arr):
    indexs = []
    values = -np.inf
    for i in range(len(arr)):
        if arr[i] > values:
            indexs = []
            indexs.append(i+1)
            values = arr[i]
        #elif arr[i] == values:
        #    indexs.append(i+1)
    return indexs