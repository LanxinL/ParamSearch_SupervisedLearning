# ParamsComp_SupervisedLearning

This code aims to hyperparameters search for supervised learning. 

The code provide a **log module** to record the hyperparameters and the corresponding result, and an **analysis module** to find a best combination of hyperparameters or a set of good combination of hyperparameters.

## Requirement
- numpy
- pandas

## Usage
### 1. log module
```
# import
form loggerToCsv import LoggerToCsv

# new logger obj
logger = LoggerToCsv('savePath', parameterDict, backUpPath='backUpPath')
# savePath is used to save all the training result
# backUpPath is used to save the traing result singlely, whose default is None
# parameterDict is a dict whose columns are the name of hyperparameters

# record best result
bestAccuracy = 0.9     # Fake data
bestAccuracyStd = 0.01 # Fake data
logger.record('bestAccuracy',bestAccuracy)
logger.record('bestAccuracyStd',bestAccuracyStd)

# save
logger.save()
```
### 2.analysis mudule
- Run `python createFakeResult.py` to create faka result data 
  - The data is saved in `path = 'result/fake.csv'`
  - The following parameters decide the distribution of the fake data
    ```                             
    dataSetNum = 4             
    paramNum = 5               
    bestParamNum = 2           
    paramRange = 2             
    ```
    - `paramNum` decides the count of the hyperparameters
    - `paramNum` - `bestParamNum` is the count of uncertain hyperparameters
      - If `paramNum` - `bestParamNum` = 0, there is a best combination of hyperparameters to each dataSet, or there are some uncertain hyperparameters.
    - `paramRange` decides the count of different value in each parameter
  - used for find the best parameters
- Run `python analysis.py` to find a best combination of hyperparameters or a set of good combination of hyperparameters.
 
 #### 2.2 test analysis mudule
 ##### 2.2.1 Exist a best combination of hyperparameters
  - Creat Fake data as following setting
    - set `dataSetNum` and `paramRange` whatever you like
      - default values are `dataSetNum = 4` and `paramRange = 2`
    ```
    paramNum = 5      
    bestParamNum = 5  
    ```
  - run `python createFakeResult.py`, then you can see:
  ```
  ============= create fake data over =================         
  ============= total param num : 5                             
  ============= uncertain param num : 0                         
  ============= total dataSet num : 4                           
  ============= length of fake data : 128                       
 ```
 - run `python analysis.py`, then you can get:
 ```
 ============= analysis data over =================             
 ============= length of data : 128                             
 ============= length of uncertain param num : 0                
 ============= length of certain param combination num : 1    
 ============= length of analyzed data : 4                      
 ```
 - 4 datasets have the same best combination of hyperparameters, so the length of analyzed data is 4
##### 2.2.2 Don't exist a best combination of hyperparameters
   - Creat Fake data as following setting
    ```
    paramNum = 5      
    bestParamNum = 3  
    ```
  - run `python createFakeResult.py`, then you can see:
  ```
  ============= create fake data over =================         
  ============= total param num : 5                             
  ============= uncertain param num : 2                         
  ============= total dataSet num : 4                           
  ============= length of fake data : 128                       
 ```
 - run `python analysis.py`, then you can get:
 ```
 ============= analysis data over =================             
 ============= length of data : 128                             
 ============= length of uncertain param num : 2                
 ============= length of certain param combination num : 4    
 ============= length of analyzed data : 16                      
 ```
 - 4 datasets have 2 uncertain hyperparameters. Each hyperparameter has 2 values. So the length of analyzed data is `2*2*4 =16`

## TODO
- [ ] Support to compare with benchmark in a pointed column
