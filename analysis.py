dirPath = 'result/'
csvName = 'fake.csv'
savePath = 'summaryFake.csv'

datasetCol = 'fakeDataSet'
compareCol = 'testAccuracy'
otherLogCols = ['runTime', 'testAccuracyStd']

import pandas as pd
from itertools import product
import numpy as np

data = pd.read_csv(dirPath+csvName)    

def getParamDict(data):
    parameters = data.columns
    paramDict = {}
    for parameter in parameters:
        paramDict[parameter] = data[parameter].drop_duplicates().to_numpy()
    return paramDict

def delResultKeys(dic, resultCols):
    for key in resultCols:
        if key in dic.keys():
            del dic[key]

paramDict = getParamDict(data)
delResultKeys(paramDict, otherLogCols + [compareCol])

maxResults = pd.DataFrame()
for dataset in paramDict[datasetCol]:
    maxDatas = data[data[datasetCol].isin([dataset])][compareCol].max() 
    maxResults = maxResults.append(data[data[compareCol].isin([maxDatas])])

diffParamDict = getParamDict(maxResults)
#delResultKeys(diffParamDict, resultCols)
delResultKeys(diffParamDict, otherLogCols + [compareCol, datasetCol])

paramComb = list(product(*list(diffParamDict.values())))

sResults = pd.DataFrame()
for diffParam in paramComb:
    filters = 1
    for col, value in zip(list(diffParamDict.keys()), diffParam):
        filters = filters & data[col].isin([value]) 
    sResults = sResults.append(data[filters])

sResults.to_csv(dirPath+savePath,index=False)

print('============= analysis data over =================')
print('============= length of data :', len(data))
print('============= length of uncertain param num :', sum([x.shape[0] -1 for x in np.asarray(list(diffParamDict.values()))]))
print('============= length of uncertain param combination num :', np.prod([x.shape for x in np.asarray(list(diffParamDict.values()))]))
print('============= length of analyzed data :', len(sResults))

# FOR TEST
#    if len(data[basic]) == 0:
#        basic = 1
#        for col, value in zip(list(diffParamDict.keys()), diffParam):
#            if sum(basic & data[col].isin([value])) == 0:
#                import pdb; pdb.set_trace()
#            basic = basic & data[col].isin([value])
#            print(col, value)
#            print(sum(basic))
        

