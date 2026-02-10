#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 15:40:18 2026

@author: fkaka

Here are the functions for saving and loading json files:
    - reusable
    - not model-specific
    - infrastructure code
"""

from pathlib import Path
import json
import pickle 
from typing import Any, Dict
import pandas as pd
def save_json(data: Dict[str,Any],filepath: Path) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath,"w") as f:
        json.dump(data,f,indent=4)
    
    
def load_json(filepath:Path)-> Dict[str,Any]:
    if not filepath.exists():
        raise FileNotFoundError(f"{filepath} dose not exist.")
    
    with open(filepath, "r") as f:
        return json.load(f)
    

def save_model(model: Any, filepath: Path)->None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath,"wb") as f:
        pickle.dump(model,f)

def load_model(filepath: Path) -> Any:
    if not filepath.exists():
        raise FileNotFoundError(f"{filepath} does not exist.")
        
    with open(filepath,"rb") as f:
        return pickle.load(f)

def load_csv(filepath: Path) -> pd.DataFrame:
    if not filepath.exists():
        raise FileNotFoundError(f"{filepath} does not exist.")
        
    return pd.read_csv(filepath)