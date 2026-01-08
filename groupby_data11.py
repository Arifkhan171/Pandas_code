import pandas as pd
vr=pd.DataFrame({"name":["arif","faiz","ajab","faiz","arif","ajab","arif","faiz","ajab",],
                 "subject1":[11,12,23,12,15,19,21,14,19],
                 "subject2":[11,12,12,14,16,18,21,32,43,]})
print(vr) #this is a random data
print('')

vr=pd.DataFrame({"name":["arif","faiz","ajab","faiz","arif","ajab","arif","faiz","ajab",],
                 "math":[11,12,23,12,15,19,21,14,19],
                 "urdu":[11,12,12,14,16,18,21,32,43,]})
print(vr.groupby("name")) #it will not show data
var2=vr.groupby("name")
for x,y in var2:
    print(x)
    print(y)

print('')
vr=pd.DataFrame({"name":["arif","faiz","ajab","faiz","arif","ajab","arif","faiz","ajab",],
                 "math":[11,12,23,12,15,19,21,14,19],
                 "urdu":[11,12,12,14,16,18,21,32,43,]})
# print(vr.groupby("name")) #it will not sshow data
var2=vr.groupby("name")
print(var2.get_group("arif"))


vr=pd.DataFrame({"name":["arif","faiz","ajab","faiz","arif","ajab","arif","faiz","ajab",],
                 "math":[11,12,23,12,15,19,21,14,19],
                 "urdu":[11,12,12,14,16,18,21,32,43,]})
# print(vr.groupby("name")) #it will not sshow data
var2=vr.groupby("name")
print(var2.min()) #min and max return maninum and maxinum data





















