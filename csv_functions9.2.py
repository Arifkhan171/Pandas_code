import pandas as pd
from pandas import read_csv


f=read_csv(r"C:\Users\pythonProject3\panda_practise.csv",)
# print(f.index)
print(f.columns)
print(f.describe())# only numerical values
print(f.head(3))
print(f.tail(3))
print(f[3:9])# print required rows

print(f.to_numpy())

print(f.sort_index(axis=0,ascending=False))

f.loc[0,"first_name"]="python" #chang spacific name
print(f)

w=f.loc[[2,3],["first_name","delivery","date"]]
print(w)

