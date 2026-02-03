#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 11:09:55 2026

@author: fkaka
"""
import pytest
from src.models.Linear_Regression import LinearRegression 
import numpy as np 


def test_valid_prediction():
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 8])  # y = 2x

    model = LinearRegression(learning_rate=0.01, nr_itr=2000)
    model.fit(X, y)

    preds = model.predict(X)
    assert np.allclose(preds,y, atol=0.5)
    

def test_input_dim():
    
    X = np.arange(100).reshape(100,1)
    y = np.arange(50)
    
    model = LinearRegression(learning_rate=0.01, nr_itr=2000)
    
    with pytest.raises(ValueError):
        
        model.fit(X, y)
        
def test_invalid_prediction_shape():
    X = np.arange(100).reshape(50,2)
    y = np.arange(50)
    
    model = LinearRegression(learning_rate=0.01, nr_itr=20)    
    model.fit(X, y)
    y_pred = model.predict(X)
    
    assert y_pred.shape == (50,)