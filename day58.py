# Day58 - Data Visualization Mini Project
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

# bar chart
plt.bar(df["Product"], df["Units_Sold"])
plt.title("Units Sold by Product in bar chart")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.show()

# scatter plot
plt.scatter(df["Price"], df["Units_Sold"])
plt.title("Price vs Units Sold in scatter plot")
plt.xlabel("Price")
plt.ylabel("Units Sold")
plt.show()