import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv('penguins (1).csv')
sns.barplot(x="island",y="bill_length_mm",data=r)
sns.set_style("white")
sns.set_context("poster",font_scale=2)

sns.despine()
plt.show()