#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 17:14:41 2026

@author: fkaka
"""

from pathlib import Path
from src.utils.io import save_json, load_json, save_model, load_model, load_csv
from sklearn.linear_model import LinearRegression

def test_save_and_load_json(tmp_path):
    
    test_data = {"learning_rate":0.01, "epochs":10}
    file_path = tmp_path / "params.json"
    save_json(test_data,file_path)
    loaded = load_json(file_path)
  
    assert loaded == test_data
    

def test_save_and_load_model(tmp_path):
    model = LinearRegression()
    
    file_path = tmp_path / "model.pkl"
    
    save_model(model, file_path)
    loaded_model = load_model(file_path)
    print('Here is the temp path',tmp_path)
    assert isinstance(loaded_model, LinearRegression)
    

def test_load_csv(tmp_path):
    df = pd.DataFrame({"a": [1, 2, 3]})
    file_path = tmp_path / "data.csv"
    df.to_csv(file_path, index=False)

    loaded_df = load_csv(file_path)

    assert loaded_df.equals(df)