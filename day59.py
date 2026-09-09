# Day59 - Data Visualization 2ndMini Project
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

# Seaborn - Count Plot

sns.countplot(x="Category", data=df)
plt.title("Number of Products by Category in count plot")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.show()


# Seaborn - Box Plot

sns.boxplot(x="Category", y="Price", data=df)
plt.title("Price Distribution by Category in box plot")
plt.xlabel("Category")
plt.ylabel("Price")
plt.show()


# Correlation

correlation = df.corr(numeric_only=True)

print("Correlation Matrix:")
print(correlation)