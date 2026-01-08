import pandas as pd

x1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
x2=pd.DataFrame({"A":[1,2,3,4],"C":[22,23,242,44]})
print(pd.merge(x1,x2,on="A"))
print("")


x1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
x2=pd.DataFrame({"A":[1,2,3,5],"C":[22,23,242,44]})
print(pd.merge(x1,x2,how="outer")) # left and right show nan values in left and right side and outer show nan data both side
print(pd.merge(x1,x2,how="outer",indicator=True)) # left and right show nan values in left and right side and outer show nan data both side
print("")

x1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
x2=pd.DataFrame({"A":[1,2,3,4],"B":[22,23,242,44]})
print(pd.merge(x1,x2,left_index=True,right_index=True)) # when x2 and x1 have same paramaters

 # concat
s1=pd.Series([1,2,3,4])
s2=pd.Series([11,31,33,43])
print(pd.concat([s1,s2])) #no difference between merg and concate


x1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
x2=pd.DataFrame({"A":[1,2],"C":[22,23]})
print(pd.concat([x1,x2],axis=1))

x1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
x2=pd.DataFrame({"A":[1,2],"C":[22,23]})
print(pd.concat([x1,x2],axis=1,join="inner")) #inner will delet missing data and outer retain nan values











