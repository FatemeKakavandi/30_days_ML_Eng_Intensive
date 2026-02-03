#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:17:59 2026

@author: fkaka
"""

import numpy as np

def train_test_split(X,y,test_ratio=0.2, random_seed=42):
    """
    return x_train, x_test, y_train, y_test
    
    Args:
        X: dataset in array form
        y: the target 
        test_ratio: the ratio of the test set 
    
    return:
        shuffled x_train,x_test,y_train,y_test
        
    Raise:
        empty dataset
        mismatched sample numbers in x, y
        test_ratio outside the boundry of (0,1)

    """
    
    if (test_ratio<0) | (1<test_ratio):
        raise ValueError('The test ratio is not acceptable')
    
    X=np.array(X)
    y = np.array(y)
    
    if len(X)!=len(y):
        raise ValueError('Mismatch number of observations')
        
    if len(X)==0:
        raise ValueError('Empty dataset')
    
    if len(y)==0:
        raise ValueError('Empty target list')
    np.random.seed(random_seed)
    index = np.arange(len(X))
    np.random.shuffle(index)
    
    X_shuffled = X[index]
    y_shuffled = y[index]
        
    X_train= X_shuffled[round(test_ratio*len(X)):]
    X_test= X_shuffled[:round(test_ratio*len(X))]
    
    y_train = y_shuffled[round(test_ratio*len(X)):]
    y_test = y_shuffled[:round(test_ratio*len(X))]
    
    return X_train, X_test, y_train, y_test


X = np.arange(100).reshape(50,2)
y = np.arange(50)
