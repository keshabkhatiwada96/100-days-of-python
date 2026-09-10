# Correlation Heatmap 3rd mini project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Creating sales dataset
data = {
    "Product": ["Laptop", "Phone", "Headphones", "Keyboard", "Monitor", "Mouse", "Tablet", "Speaker"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories",
                 "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [900, 600, 80, 50, 300, 30, 450, 120],
    "Units_Sold": [12, 25, 40, 35, 18, 60, 20, 30],
    "Rating": [4.5, 4.3, 4.2, 4.0, 4.4, 4.1, 4.6, 4.2]
}

df = pd.DataFrame(data)
print("Sales Data:")
print(df)

# Correlation
correlation = df.corr(numeric_only=True)
print("Correlation Matrix:")
print(correlation)

# Heatmap
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()