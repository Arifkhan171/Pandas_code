import pandas as pd

x=[1,2,3,4]
x2=pd.Series(x,index=['a','b','c','d'],dtype='float',name='python series')
print(x2)
print(type(x2))
print(x[2])
print(" ")

# make series of dictionary
dic={"name":['python','java'],"rank":[1,2],"learn":[1,0]}
x3=pd.Series(dic)
print(x3)
print("")


# addition of two series
x=pd.Series([1,2,3,4])
x2=pd.Series([1,2,3,4,5,6,7])
print(x+x2)
