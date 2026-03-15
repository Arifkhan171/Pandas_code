import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv('penguins (1).csv').head(150)
sns.pairplot(r,hue="sex",palette="Dark2",kind="scatter")#scattr, hist,reg,kde
plt.show()