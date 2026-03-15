import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv('penguins (1).csv').head(150)
sns.stripplot(x="island",y="flipper_length_mm",data=r,color="r",hue="sex",size=7,marker="*")#jitter=2 show displacment
plt.show()