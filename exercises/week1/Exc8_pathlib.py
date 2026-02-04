#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:43:10 2026

@author: fkaka
"""

from  pathlib import Path

p = Path('/etc')/"init.d"/"reboot"

print(p.exists()) 
print(p.is_file())
print(p.is_dir())
print(p.name)
print(p.suffix)
print(p.stem)

# find all the entries in current files 
current_p = Path('.')
for entry in current_p.iterdir():
    print(entry)
    
# Find directions in the current path
dirs = [x for x in current_p.iterdir() if x.is_dir()]
print(dirs)

# find all files with .py extensions
for py_file in Path('.').glob('**/*.py'):
    print(py_file)

# Writing and reading files    
file = Path("example.txt")
file.write_text("Hello World")
print(file.read_text())


# Make dir
new_dir = Path('mydir')
new_dir.mkdir(exist_ok=True)

# Delete dir
new_dir.rmdir()

# Delete a file 

Path('example.txt').unlink()