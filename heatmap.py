import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
var=np.linspace(1,10,20).reshape(4,5)
y={"fontsize":20,"color":"g"}
sns.heatmap(var,annot=True,annot_kws=y,linewidth=6,linecolor="y")
plt.show()
