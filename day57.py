#Correlation and Heatmaps
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# creating dataframe
data = {
"Name" :["Keshab","arthur","ram","sita","hari"],
"Age" :[20,22,24,19,21],
"Study_Hours":[3,4,7,6,5],
"Marks":[84,86,93,89,90],
}
df = pd.DataFrame(data)
correlation = df.corr(numeric_only=True)
print(correlation)

# creating heatmap
sns.heatmap(correlation, annot=True)
plt.show()