import pandas as pd
from markdown_it.rules_inline.backticks import regex
from pandas import read_csv

# csv=read_csv("panda practise2.csv")
#print(csv)

# r=csv.replace(to_replace="Genderfluid",value="male")
# print(r)

# csv=read_csv("panda practise2.csv")
# print(csv.replace (["F"],["f"],regex=True))

# csv=read_csv("panda practise2.csv")
# print(csv.replace({"gender":'[e]'},"ee",regex=True))

#    interpolate
csv=read_csv("panda practise2.csv")
# r=csv.interpolate() # work on no and it is linear and having lot of parameters with methid function
# print(r) #if all values are same than it also work on axis

# r=csv.interpolate(limit=2)
# print(r)

r=csv.interpolate(limit_direction="forward")
print(r)

# r=csv.interpolate(limit_area="inside") #inside will change all values and out side will show all original nan values
# # print(r)

# r=csv.interpolate(limit_direction="forward",inplace=True)# by sitting inplace your original data is changes and when you work it wil show you that new data
# print(r)
#



