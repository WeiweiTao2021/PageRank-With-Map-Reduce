import pandas as pd
import numpy as np

import sys
import os
os.chdir('/Users/weiweitao/Desktop/Stony Brook/Fall 2021 Courses/AMS598/project2/map1')


df1=pd.read_csv("xaa_map1.txt", sep=',',header =0 )
print("Initial Shape: ",df1.shape)

for i in ['b', 'd', 'f', 'h', 'j', 'n', 'o', 'r', 's', 't']:
    print('reading file {}'.format(i))
    df2=pd.read_csv("xa{}_map1.txt".format(i), sep=',',header =0)
    print("DF2 Shape: ",df2.shape)
    df_merge = pd.merge(left=df1, right=df2, how='outer', left_on='0', right_on='0')
    df_merge['combined']= df_merge['new_x'].str.strip('[]') + ', ' + df_merge['new_y'].str.strip('[]')
    df1 = df_merge.drop(columns = ['new_x', 'new_y'])
    df1 = df1.rename(columns={"combined": "new"})
    print("Combined Shape: ",df1.shape)

df1.to_csv('reduce1.txt', sep=',', index = False)
