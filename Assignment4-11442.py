# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 19:12:38 2018

@author: Siva

>>> x = np.array([1, 2, 3, 5])
>>> N = 3
>>> np.vander(x, N)
array([[ 1,  1,  1],
       [ 4,  2,  1],
       [ 9,  3,  1],
       [25,  5,  1]])

"""
import numpy as np

def getResultArray(inputVector,N=0,increasing=False):
    if N==0:
        N=len(inputVector)
    #Create the output vector initialized with ones
    outputVector=np.ones((len(inputVector),N),dtype=int)
    #The counter below will traverse the inputVector
    counter=0
    for row in range(outputVector.shape[0]):
        for col in range(outputVector.shape[1]):
            #if not increasing, put X^n-1,X^n-2 etc. Else put X^0,X^1 etc
            if not increasing:
                cellValue=inputVector[counter]**(N-col-1)
            else:
                cellValue=inputVector[counter]**col
            #Set the cell value
            outputVector[row,col]=cellValue
        counter+=1  
    return outputVector

inputVector=np.array([1, 2, 3, 5],dtype=int)

outputVector=getResultArray(inputVector)
print(outputVector)

outputVector=getResultArray(inputVector,3)
print(outputVector)

outputVector=getResultArray(inputVector,3,False)
print(outputVector)

outputVector=getResultArray(inputVector,3,True)
print(outputVector)