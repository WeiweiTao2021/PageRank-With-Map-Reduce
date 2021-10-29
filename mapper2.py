import pandas as pd
import numpy as np

import sys
import os
os.chdir('/Users/weiweitao/Desktop/Stony Brook/Fall 2021 Courses/AMS598/project2/map1')


df1=pd.read_csv("reduce1.txt", sep=',',header=0)
print("Initial Shape: ",df1.shape)

df1['pr'] = 1/len(df1)

df2 = df1.dropna()
df2['rate'] = df2['new'].apply(lambda x:  1/len(x))
df2['new'] = df2['new'].apply(lambda x:  x.split(','))

#------------- other loops
def pr_update(df, prout):
    df_1 = df.explode('new')
    
    df_1['update'] = df_1['rate']*df_1['pr'] 
    df_1['new'] = df_1['new'].astype(float)
    df_1 = df_1.dropna()
    df_1['new'] = df_1['new'].astype(int)
    
    df_2 = df_1.groupby('new').sum('update')
    df_2['pr'] = 0.1/len(df1) + 0.9*df_2['update']
    
    
    df_3 = pd.merge(left=df2[['0', 'new', 'rate']], 
                   right=df_2['pr'], how='left', 
                   left_on='0', right_index=True)
    
    
    df_3.to_csv(prout, sep=',', index = False)
    return df_3

df5 = pr_update(df2, 'pr1.txt')
df6 = pr_update(df5, 'pr2.txt')
df7 = pr_update(df6, 'pr3.txt')
df8 = pr_update(df7, 'pr4.txt')
df9 = pr_update(df8, 'pr5.txt')
