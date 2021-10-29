#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:45:25 2021

@author: weiweitao
"""

import os
filepath = os.getcwd()

for i in range(ord('a'), ord('t')+1):
    filename = 'analysis_xa{}.py'.format(chr(i))
    temp_path = filepath + filename
    
    with open(filename, 'w') as f:
        f.write('''import pandas as pd
import numpy as np


df=pd.read_csv("xa{}", sep=',',header =None, error_bad_lines=False)
df1 = df.groupby(0)[1].apply(list).reset_index(name='new')
df1.to_csv('xa{}_map1.txt', sep=',', index = False)
              '''.format(chr(i),chr(i)))
        
        
        
    