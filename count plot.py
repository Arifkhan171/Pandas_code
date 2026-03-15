import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv('penguins (1).csv').head(150)
sns.countplot(x=r.island,hue=r.sex,palette="bwr")
plt.show()