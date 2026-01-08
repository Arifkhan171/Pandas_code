import pandas as pd


d1=pd.DataFrame({"arif":[2,3,4,5],"gul":[11,12,13,14]})
# d2=pd.DataFrame({"ajab":[21,31,41,51],"sattar":[22,22,23,24]})
d2=pd.DataFrame({"ajab":[21,31],"sattar":[22,22]})
print(d1.join(d2))
print('')



d1=pd.DataFrame({"arif":[2,3,4,5],"gul":[11,12,13,14]})
d2=pd.DataFrame({"ajab":[21,31,41,51],"sattar":[22,22,23,24]})
d2=pd.DataFrame({"ajab":[21,31],"sattar":[22,22]})
print(d2.join(d1)) #it will only show two data
print("")
print(d2.join(d1,how="outer"))# outer works as a union and inner work as a intersection ,also use right and left side



# APPEND FUNCTION USE TO WORK TO ADD DATAFRAMES the deffernce is that it also work on same name
d1=pd.DataFrame({"arif":[2,3,4,5],"gul":[11,12,13,14]})
d2=pd.DataFrame({"ajab":[21,31],"gul":[22,22]})
print(d1._append(d2))