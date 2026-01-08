import pandas as pd
var={"A":[1,2,3,4,5,],"B":[11,22,33,44,55,]} # size must be same
var2=pd.DataFrame(var)
print(var2)
print("")

var2.insert(1,"C",[2,4,65,7,5])
print(var2)
print("")
var=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
#print(var)
var["c"]=var["A"][:2]
var.insert(2,"d",var["A"])
print(var)
print("")


var=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,22,33,44,55]})
var["c"]=var["A"][:2]
print(var)
print("")
var.pop("B")
print(var)
print("")
