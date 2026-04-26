import pandas as pd
x=[1,2,3,4]
x2=pd.DataFrame(x)
print(x2)
print("  ")


# make datafram from dictionary
dic={"name":['python','java'],"rank":[1,2],"learn":[1,0]}
x3=pd.DataFrame(dic)
print(x3)
print("")

x3=pd.DataFrame(dic,columns=["name"])
print(x3)
print(" ")


print(x3["name"][1])

