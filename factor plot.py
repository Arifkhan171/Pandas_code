import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv('penguins (1).csv')
sns.catplot(x="island",y="bill_length_mm",data=r,hue="sex",kind="boxen")# Options are 'strip', 'swarm', 'box', 'boxen', 'violin', 'bar', 'count', and 'point'.

plt.show()