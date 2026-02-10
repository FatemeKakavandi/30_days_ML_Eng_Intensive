#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:55:36 2026

@author: fatemeh kakavandi

"""

# convert a python object to a string 
# dumps return a string 

import json
data = {'name':'Alice','age':30,'language':['python','c++']}

json_str = json.dumps(data)
print(json_str)

# customizing json string
new_json_str = json.dumps(data,indent=2,sort_keys=True)
print('customised json string',new_json_str)

# write Json to a file 
data =[1,2,3]

with open('nums.json','w') as f:
    json.dump(data,f)
    

# convert a json string to a python data structure
# loads takes a string (or bytes) and returns a Python object.
json_data = '{"name":"Bob","active":true,"score":null}'
data = json.loads(json_data)
print(data, type(data))

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

p = Point(2,4)

print(json.dumps(p,default=lambda o:{"x":o.x,"y":o.y}))