# Pandas Merging and Combining DataFrames

import pandas as pd
#first DataFrame
students = {

    "Student_ID": [101, 102, 103, 104],

    "Name": ["Keshab", "Ram", "Sita", "Hari"]

}

df_students = pd.DataFrame(students)

print("Student Data:")
print(df_students)


print("------------------------")
#Second DataFrame
marks = {

    "Student_ID": [101, 102, 103, 104],

    "Marks": [80, 65, 90, 72]

}

df_marks = pd.DataFrame(marks)

print("Marks Data:")
print(df_marks)
print("-----------")
#mrging both dataFrames using Student_ID
df = pd.merge(df_students, df_marks, on="Student_ID")
print("Merged Data:")
print(df)
print("---------------")
# creating another dataFrame with Course informatin
courses = {

    "Student_ID": [101, 102, 103, 104],

    "Course": ["BIT", "BCA", "BIT", "BCA"]

}
df_courses = pd.DataFrame(courses)
print("Course Data:")
print(df_courses)
print("------------------------")
df = pd.merge(df, df_courses, on="Student_ID")      # Merge student data with course data
print("Final Merged Data:")
print(df)