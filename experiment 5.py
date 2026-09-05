# Program 1: Indexing and Slicing Using a NumPy Array
import numpy as np

marks_arr = np.array([56, 78, 90, 65, 88, 72, 60, 95])
print("Original Array")
print(marks_arr)
print("First Element:", marks_arr[0])
print("Last Element:", marks_arr[-1])
print("Array from Index 1 to 4:")
print(marks_arr[1:5])
print("Every Second Element:")
print(marks_arr[::2])


# Program 2: Indexing and Slicing Using a Pandas DataFrame
import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3.csv")
print("First Five Rows")
print(df.head())
print("Student_ID Column")
print(df["Student_ID"])
print("First Three Rows")
print(df[0:3])


# Program 3: Using loc() and iloc() on the Dataset
print("Using loc()")
print(df.loc[0:4, ["Age", "GPA"]])

print("Using iloc()")
print(df.iloc[0:5, 0:2])


# Program 4: Boolean Indexing
filtered = df[df["Attendance_Rate"] > 90]
print("Students with Attendance Rate above 90")
print(filtered.head())


# Program 5: Reshaping a NumPy Array
age_values = df["Age"].head(12).to_numpy()

print("Original Array")
print(age_values)
print("Original Shape")
print(age_values.shape)

reshaped = age_values.reshape(3, 4)
print("Reshaped Array")
print(reshaped)
print("New Shape")
print(reshaped.shape)
