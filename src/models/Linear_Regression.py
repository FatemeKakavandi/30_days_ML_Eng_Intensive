#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:24:58 2026

@author: fkaka
"""
import numpy as np

class LinearRegression():
    def __init__(self, learning_rate: float=0.01,nr_itr:int=100):
        """
        Linear Regression with Gradient Descent 
        Parameter:
            learning rate : float 
            step size for gradient descent 
            nr_itr : int 
            number of training iterations 
        """
        self.learning_rate = learning_rate
        self.nr_itr = nr_itr
        self.weights:np.ndarray|None = None
        self.bias:float|None = None
        
    def fit(self, X:np.ndarray ,y:np.ndarray)-> None:
        
        """
        Train the linear regression model using gradient descent.

        Parameters
        ----------
        X : np.ndarray of shape (n_samples, n_features)
        y : np.ndarray of shape (n_samples,)
        """
        
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        if X.ndim!=2:
            raise ValueError('X must be a 2D array')
            
        if y.ndim!=1:
            raise ValueError('y mush be 1D array')
        for i in range(self.nr_itr):
            y_pred = X @ self.weights + self.bias
            dw = (1/(len(X))) * X.T @(y_pred-y)
            db = (1/(len(X))) * np.sum(y_pred - y)
            self.weights -= self.learning_rate*dw
            self.bias -= self.learning_rate*db
        
        
        
    def predict(self, X:np.ndarray)-> np.ndarray:
        
        """
        Predict using the trained model.

        Parameters
        ----------
        X : np.ndarray of shape (n_samples, n_features)
    
        Returns
        -------
        np.ndarray of shape (n_samples,)
        """
        if self.weights is None or self.bias is None:
           
            raise ValueError('the model has not been train yet call fit() funtion first.')
           
        if X.ndim!=2:
            raise ValueError('X must be a 2D array')
           
        return X @ self.weights + self.bias
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


