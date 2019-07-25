import pandas as pd
import argparse

class loggerToCsv(object):
    def __init__(self, savePath, parameterDict=None, backUpPath=None):
        self.savePath = savePath
        self.backUpPath = backUpPath
        self._creatLogDf(parameterDict)

    def _creatLogDf(self, parameterDict):
        if isinstance(parameterDict, argparse.Namespace):
            parameterDict = vars(parameterDict)
        else:
            assert isinstance(parameterDict, dict)
        self.logDf = pd.DataFrame(parameterDict,index=[0]) if args.savePath else None

    def record(self, colName, value):
        self.logDf[colName] = value

    def save(self):
        if not os.path.isfile(self.savePath):
             resultDateFrame.to_csv(self.savePath,index=False)
        else:
            finamFile = pd.read_csv(self.savePath)
            finamFile = finamFile.append(self.logDf, ignore_index=True)
            finamFile.to_csv(self.savePath,index=False)
        if args.backUpPath is not None:
            self.logDf.to_csv(self.backUpPath,index=False)

