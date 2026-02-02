#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:56:20 2026

@author: fkaka
"""

import numpy as np
from exercises.week1.train_test_split_custom import train_test_split
import pytest

def test_split_shapes():
    X= np.arange(100).reshape(50,2)
    y= np.arange(50)
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_ratio=0.2)
    
    assert len(X_test)==10
    assert len(X_train)==40
    assert len(y_train)==40
    assert len(y_test)==10
    


def test_reproducibility():
    X = np.arange(20).reshape(10,2)
    y = np.arange(10)
    
    split1 = train_test_split(X,y,random_seed=42)
    split2 = train_test_split(X,y,random_seed=42)
    
    assert np.array_equal(split1[0],split2[0])
    assert np.array_equal(split1[2],split2[2])
    
    
def test_invalid_ratio():
    X=np.arange(10)
    y = np.arange(10)
    
    with pytest.raises(ValueError):
        train_test_split(X,y,test_ratio=1.4)
        

def test_mismatched_length():
    X=np.arange(10)
    y = np.arange(5)
    
    with pytest.raises(ValueError):
        train_test_split(X,y)
        

def test_zero_length():
    X = []
    y = []
    
    with pytest.raises(ValueError):
        train_test_split(X,y)
    