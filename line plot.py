import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
v=pd.read_csv("penguins (1).csv").head(200)
sns.lineplot(x='bill_length_mm',y='flipper_length_mm',data=v,hue='sex',
             style="sex",palette="Accent",markers=["o",">"])
plt.title("python",fontsize=15)
plt.grid()
plt.show()