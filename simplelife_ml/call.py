# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:39:23 2018

@author: olgierd baranski, pwc switzerland
"""

import matplotlib.pyplot as plt
import os.path as path
import os
import seaborn as sns
import pandas as pd

try:
    import simplelife.simplelife as simplelife
except ImportError:
    import simplelife
    

def save_totres_to_xls(data, name):
    base_path = path.abspath(path.dirname(__file__))
    output_path = path.join(base_path, '0_output')
    name2 = path.join(output_path, name)
    data.to_excel(name2)
    return None

def save_totres_to_csv(data, name):
    base_path = path.abspath(path.dirname(__file__))
    output_path = path.join(base_path, '0_output')
    name2 = path.join(output_path, name)
    data.to_csv(name2)
    return None

###############################################################################
    
items_tot = ['PVFP']

fpol = 1
lpol = 30

sur_is = 10
int_is = 10
mrt_is = 10

sur_ls = 10
int_ls = 10
mrt_ls = 10

sur_fs = 0
int_fs = 0
mrt_fs = 0



sur_rate_step = 5
int_rate_step = 1
mrt_rate_step = 2 

d = []
i = 0

###############################################################################

for mrt_i in range(mrt_fs, mrt_ls + 1):
    for int_i in range(int_fs, int_ls +1):
        for sur_i in range(sur_fs, sur_ls + 1):
            i += 1
            print('now in ', 'i =' , i ,  'mrt =', mrt_i, 'int =', int_i, 'sur =', sur_i )
            
            mrt_mult = 1 - (mrt_rate_step * (mrt_is)/2)/100 + ((mrt_i) * mrt_rate_step)/100
            int_adj = 0 - (int_rate_step * (int_is)/2)/100 + ((int_i) * int_rate_step)/100            
            sur_mult = 1 - (sur_rate_step * (sur_is)/2)/100 + ((sur_i) * sur_rate_step)/100
            
            model = simplelife.build(True , mrt_mult , int_adj , sur_mult , mrt_i , int_i , sur_i)
            pvfp = 0
            for polid in range(fpol,lpol + 1):                
                pvfp += model.Projection[polid].PVFP(0)
                
            d.append(( mrt_mult, int_adj, sur_mult, pvfp))

df_sensis= pd.DataFrame(d, columns=('mrt_mult', 'int_adj','sur_mult',  'PVFP'))
save_totres_to_xls(df_sensis, name = 'sensi_output.xlsx')
save_totres_to_csv(df_sensis, name = 'sensi_output.csv')
print ('FINISHED')
