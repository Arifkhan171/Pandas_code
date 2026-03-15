import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv('penguins (1).csv')# FacetGrid is used to plot seprate graph
f=sns.FacetGrid(r,col="sex")
f.map(plt.scatter,"island","bill_length_mm").add_legend()
plt.show()