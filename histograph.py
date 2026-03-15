import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
r=pd.read_csv("penguins (1).csv").head(150)
print(r)
sns.histplot(r.bill_length_mm,bins=[32,34,36,38,40,42,44,46,48],kde=True,
             color="r")# bins use to organize data in graph
plt.show()

