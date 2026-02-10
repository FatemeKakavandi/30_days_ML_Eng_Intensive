#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 14:30:17 2026

@author: fkaka
"""

import pickle

# writing python objects into pickles
data = {"x":[2,3,4],"y":42}

with open("mydata.pkl","wb") as f:
    pickle.dump(data,f)
    
# Loading pkl files into python objects    
with open("mydata.pkl","rb") as f:
    data = pickle.load(f)
print(data,type(data))

# In Memory Pickling 

b = pickle.dumps([1,2,3])
obj = pickle.loads(b)
print(obj)