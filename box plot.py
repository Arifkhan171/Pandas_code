import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv('penguins (1).csv')
sns.boxplot(x="island",y="flipper_length_mm",data=r,hue="sex",showmeans=True,)
plt.show()



