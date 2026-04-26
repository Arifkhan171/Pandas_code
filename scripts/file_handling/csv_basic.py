import pandas as pd
dic={"a":[1,2,3,4,5],"b":[11,12,13,14,15]}
d=pd.DataFrame(dic)
d.to_csv("new-panda1.0.csv")
d.to_csv("new-panda1.1.csv",index=False)
d.to_csv("new-panda1.2.csv",index=False,header=[1,2])
print(d)




