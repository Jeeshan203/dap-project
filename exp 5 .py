import numpy as np
import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3.csv")

# ================================================
# Program 1: Indexing and Slicing Using a NumPy Array
# ================================================
attendance_arr = df["Attendance_Rate"].to_numpy()
print("Total Values in Array:", len(attendance_arr))
print("Original Array")
print(attendance_arr)
print("First Element:", attendance_arr[0])
print("Last Element:", attendance_arr[-1])
print("Array from Index 1 to 4:")
print(attendance_arr[1:5])
print("Every Second Element:")
print(attendance_arr[::2])
# ================================================
# Program 2: Indexing and Slicing Using a Pandas DataFrame
# ================================================
print("\n================================================")
print("Program 2: Indexing and Slicing Using a Pandas DataFrame")
print("================================================")
print("Total Rows in Dataset:", len(df))
print("Full Dataset")
print(df)
print("Student_ID Column")
print(df["Student_ID"])
print("First Three Rows")
print(df[0:3])

# ================================================
# Program 3: Using loc() and iloc() on the Dataset
# ================================================
print("\n================================================")
print("Program 3: Using loc() and iloc()")
print("================================================")
print("Using loc()")
print(df.loc[:, ["Age", "GPA"]])
print("Using iloc()")
print(df.iloc[:, 0:2])

# ================================================
# Program 4: Boolean Indexing
# ================================================
print("\n================================================")
print("Program 4: Boolean Indexing")
print("================================================")
filtered = df[df["Attendance_Rate"] > 90]
print("Number of Students with Attendance Rate above 90:", len(filtered))
print(filtered)

# ================================================
# Program 5: Reshaping a NumPy Array
# ================================================
print("\n================================================")
print("Program 5: Reshaping a NumPy Array")
print("================================================")
age_values = df["Age"].to_numpy()
print("Original Array")
print(age_values)
print("Original Shape")
print(age_values.shape)
reshaped = age_values.reshape(1000, 10)
print("Reshaped Array")
print(reshaped)
print("New Shape")
print(reshaped.shape)