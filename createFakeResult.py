import pandas as pd
from itertools import product
import numpy as np

path = 'result/fake.csv'

dataSetNum = 4
paramNum = 5
bestParamNum = 3
paramRange = 2

fakeDataSets = []
for i in range(dataSetNum):
    fakeDataSets += ['fakeDataSet_'+str(i)]

fakeParams = []
for i in range(paramNum):
    fakeParams += ['fakeParam_'+str(i)]

fakeParmValue = np.repeat([np.arange(paramRange)], paramNum, axis=0)

allFakeParamComb = product(fakeDataSets, *list(fakeParmValue))

fakeResults = pd.DataFrame(columns = ['fakeDataSet'] + fakeParams + ['testAccuracy', 'runTime', 'testAccuracyStd'])
for i, fakeParamComb in enumerate(allFakeParamComb):
    if np.asarray(fakeParamComb[1:bestParamNum+1]).all() == 1:
        fakeResults.loc[i] = list(fakeParamComb) + [np.random.rand()*0.5+0.5, np.random.rand(), np.random.rand()]
    else:
        fakeResults.loc[i] = list(fakeParamComb) + [np.random.rand()*0.5, np.random.rand(), np.random.rand()]

fakeResults.to_csv(path, index=False)

print('============= create fake data over =================')
print('============= total param num :', paramNum)
print('============= uncertain param num :', paramNum - bestParamNum)
print('============= total dataSet num :', dataSetNum)
print('============= length of fake data :', len(fakeResults))



