import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv("penguins (1).csv").head(10)
print(r)
sns.scatterplot(x=r.bill_length_mm,y=r.flipper_length_mm,hue=r.sex,style=r.sex,sizes=[100,40])
plt.show()




