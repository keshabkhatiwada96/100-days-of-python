# Matplotlib: Histogram and Pie Chart
import matplotlib.pyplot as plt

# histogram chart
students = ['keshab', 'harka', 'rabi', 'balen']
marks = [89, 45, 94, 99]
plt.hist(marks)
plt.title("Marks in Nepali in histogram")  # title of the figure
plt.xlabel("marks")  # X-axis name
plt.ylabel("number of students")  # Y-axis name
plt.show()

# pie chart
plt.pie(marks, labels=students)
plt.title("Marks in Nepali in pie chart")  # title of the figure
plt.xlabel("marks")  # X-axis name
plt.ylabel("number of students")  # Y-axis name
plt.show()