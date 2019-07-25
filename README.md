# ParamsComp_SupervisedLearning

This code aims to hyperparameters search for supervised learning. 

The code provide a log module to record the hyperparameters and the corresponding result, and a analysis module to find a best combination of hyperparameters or a set of good combination of hyperparameters.

## Requirement
- numpy
- pandas

## Usage
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
 
 ## test
 ### Exist a best combination of hyperparameters
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
 ### Don't exist a best combination of hyperparameters
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

## `TODO`
- [ ] Create loggerToCsv to save the best result in a constant csv file. 
