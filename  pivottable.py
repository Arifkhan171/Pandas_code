import pandas as pd
from numpy.distutils.system_info import agg2_info

# d1=pd.DataFrame({"days":[2,3,4,5],"math":[11,12,13,14],"eng":[21,31,41,15]})
# print(pd.melt(d1,id_vars="days"))# change data horizantaly/ can change variable_name and value_name

d1=pd.DataFrame({"days":[2,3,4,5],"students":["a","b","c","d"],"math":[11,12,13,14],"eng":[21,31,41,15]})
# print(d1)
# print(d1.pivot(index="days",columns="students",values="eng"))
print(d1.pivot(index="students",columns="days",))

