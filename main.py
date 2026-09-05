"""
Experiment 5: Perform Indexing, Slicing, and Reshaping Operations
on a Dataset Using Pandas and NumPy
Dataset Used: student_dropout_dataset_v3.csv
"""

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 8)
pd.set_option('display.width', 120)

# -------------------------------------------------------------
# Step 1: Load the dataset
# -------------------------------------------------------------
df = pd.read_csv("student_dropout_dataset_v3.csv")
print("="*70)
print("Dataset Shape:", df.shape)
print("="*70)
print("\nFirst 5 Records")
print(df.head())

# -------------------------------------------------------------
# Step 2: NumPy Array - Indexing and Slicing
# (using CGPA column converted to a NumPy array)
# -------------------------------------------------------------
cgpa_arr = df["CGPA"].to_numpy()

print("\n" + "="*70)
print("NUMPY ARRAY INDEXING AND SLICING (CGPA column)")
print("="*70)
print("Array length:", cgpa_arr.shape)
print("First Element:", cgpa_arr[0])
print("Last Element:", cgpa_arr[-1])
print("Elements from index 5 to 10:", cgpa_arr[5:11])
print("Every 1000th element:", cgpa_arr[::1000])

# -------------------------------------------------------------
# Step 3: Pandas DataFrame Indexing (column access, row slicing)
# -------------------------------------------------------------
print("\n" + "="*70)
print("PANDAS DATAFRAME INDEXING (column access)")
print("="*70)
print("\n'CGPA' column (first 5 values):")
print(df["CGPA"].head())

print("\nRow slice df[10:15]:")
print(df[10:15][["Student_ID", "Age", "Department", "CGPA", "Dropout"]])

# -------------------------------------------------------------
# Step 4: Label-based indexing using loc[]
# -------------------------------------------------------------
print("\n" + "="*70)
print("LABEL-BASED INDEXING USING loc[]")
print("="*70)
print(df.loc[0:4, ["Student_ID", "Department", "CGPA", "Attendance_Rate"]])

# -------------------------------------------------------------
# Step 5: Integer-based indexing using iloc[]
# -------------------------------------------------------------
print("\n" + "="*70)
print("INTEGER-BASED INDEXING USING iloc[]")
print("="*70)
print(df.iloc[0:5, 0:5])

# -------------------------------------------------------------
# Step 6: Boolean Indexing
# -------------------------------------------------------------
print("\n" + "="*70)
print("BOOLEAN INDEXING")
print("="*70)
high_risk = df[(df["Dropout"] == 1) & (df["Attendance_Rate"] < 60)]
print(f"Students who dropped out AND had Attendance_Rate < 60: {len(high_risk)}")
print(high_risk[["Student_ID", "Attendance_Rate", "CGPA", "Dropout"]].head())

low_cgpa = df[df["CGPA"] < 1.0]
print(f"\nStudents with CGPA < 1.0: {len(low_cgpa)}")
print(low_cgpa[["Student_ID", "CGPA", "Department", "Dropout"]].head())

# -------------------------------------------------------------
# Step 7: Reshaping a NumPy Array
# -------------------------------------------------------------
print("\n" + "="*70)
print("RESHAPING A NUMPY ARRAY")
print("="*70)
# Take the first 20 CGPA values (1D array of 20 elements)
sample = cgpa_arr[:20]
print("Original Array (shape {}):".format(sample.shape))
print(sample)

reshaped_4x5 = sample.reshape(4, 5)
print("\nReshaped to (4,5):")
print(reshaped_4x5)

reshaped_5x4 = sample.reshape(5, 4)
print("\nReshaped to (5,4):")
print(reshaped_5x4)

reshaped_2x2x5 = sample.reshape(2, 2, 5)
print("\nReshapesd to (2,2,5):")
print(reshaped_2x2x5)

# -------------------------------------------------------------
# Step 8: Summary
# -------------------------------------------------------------
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print(f"Total students: {len(df)}")
print(f"Dropout count: {df['Dropout'].sum()}  ({df['Dropout'].mean()*100:.2f}% dropout rate)")
print(f"Average CGPA: {df['CGPA'].mean():.2f}")