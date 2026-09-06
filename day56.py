# Seaborn basics
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# creating dataframe
data = {
    "Name": ["Keshab", "Ram", "Sita", "Hari", "Rita"],
    "Course": ["BIT", "BCA", "BIT", "BCA", "BIT"],
    "Marks": [85, 70, 90, 65, 80]
}
df = pd.DataFrame(data)
print(df)

# count plot
sns.countplot(x="Course", data=df)
plt.title("Number of students by course in count plot")   # title of the figure
plt.xlabel("course")                        # X-axis name
plt.ylabel("number of students")            # Y-axis name
plt.show()

# box plot
sns.boxplot(x="Course", y="Marks", data=df)
plt.title("Marks distribuion by course in box plot")   # title of the figure
plt.xlabel("course")                        # X-axis name
plt.ylabel("marks")                       # Y-axis name
plt.show()

# violin plot
sns.violinplot(x="Course", y="Marks", data=df)
plt.title("Marks distribution by course in viloin plot")   # title of the figure
plt.xlabel("course")                        # X-axis name
plt.ylabel("marks")                         # Y-axis name
plt.show()

# pair plot
sns.pairplot(df)
plt.show()