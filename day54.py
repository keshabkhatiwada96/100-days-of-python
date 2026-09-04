# Metplotlib basics

import matplotlib.pyplot as plt

# line graph charts
students = ['keshab','harka','rabi','balen']
marks = [89,45,94,99]
plt.plot(students,marks)
plt.title("Marks in Nepali in line graph charts ")   #title of the figure
plt.xlabel("students")     #X-axis name
plt.ylabel('marks')                     #Y-axis name
plt.show()

# marks in bar chart
plt.bar(students,marks)
plt.title('marks in nepali marks in bar chart')      #title of the figure
plt.xlabel('studnets')  #X-axis name
plt.ylabel('marks')                #Y-axis name
plt.show()

# scatter plot chart
plt.scatter(students, marks)
plt.title("student Marks in scatter plot chart")       #title of figure
plt.xlabel("students")           #x-axis name
plt.ylabel("marks")          #y-axis name
plt.show()