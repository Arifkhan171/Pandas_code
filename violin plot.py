import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv('penguins (1).csv').head(150)
sns.violinplot(x=r.island,y=r.bill_length_mm,hue=r.sex,linewidth=3,palette="Dark2",
              saturation=.8,split=True,inner="point")
plt.show()
