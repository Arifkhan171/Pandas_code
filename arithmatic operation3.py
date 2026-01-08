import pandas as pd
x=pd.DataFrame({"no":[48,78,88,14],"rank":[5,7,8,2]})
print(x)
print("")

x["multiple"]=x["no"]*x["rank"]
x["pass"]=x["no"]>=50
x["fail"]=x["no"]<=50
x["percentage"]=(x["no"]*x["rank"])/100
print(x)

