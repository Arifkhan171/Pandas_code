

import pandas as pd
from pandas import read_csv

csv=read_csv("panda practise2.csv")
print(csv)
print('')

csv=read_csv("panda practise2.csv")
print(csv.dropna())
print('')

csv=read_csv("panda practise2.csv")
print(csv.dropna(axis=1))
print('')


csv=read_csv("panda practise2.csv")
print(csv.dropna(how="any")) #remove all nan values

csv=read_csv("panda practise2.csv")
print(csv.dropna(how="all"))# will remove a particular row all with null values


csv=read_csv("panda practise2.csv")
print(csv.dropna(subset=["prices"])) # remove a particular colum null values

# csv=read_csv("panda practise2.csv")
# print(csv.dropna(thresh=1)) # will drop column with null values of spacified


#      fillna
csv=read_csv("panda practise2.csv")
print(csv.fillna( "python"))

csv=read_csv("panda practise2.csv")
print(csv.fillna({"gender":"male","prices":"00001"}))

csv=read_csv("panda practise2.csv")
print(csv.fillna(method="ffill"))

csv=read_csv("panda practise2.csv")
print(csv.fillna(method="ffill",axis=1))

csv=read_csv("panda practise2.csv")
print(csv.fillna(12,inplace=True)) #inplace function will create new file and make changes


csv=read_csv("panda practise2.csv")
print(csv.fillna("python",limit=2))
