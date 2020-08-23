import pandas as pd
import numpy as np


df = pd.DataFrame({'Country':['Korea','Japan'], 'Population':[50,130],'Ethenic': ['mongolian','pacific']})
print(df)


train_A = [1,2,3,4,5]
train_B = [1,2,3,4,5]

A_arr = np.array(train_A)
B_arr = np.array(train_B)

#denom = np.matmul(A_arr.transpose(), A_arr)
#num = np.matmul(A_arr.transpose(), B_arr)
denum = A_arr.transpose().dot(A_arr)
num = A_arr.transpose().dot(B_arr)
slope = num/denum

