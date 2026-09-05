# ================================================
# Program 1: Loading the Dataset
# ================================================
import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3.csv")
print("First Five Records")
print(df.head())


# ================================================
# Program 2: Computing Statistics
# ================================================
print("\n================================================")
print("Program 2: Summary Statistics")
print("================================================")
print(df[["Age", "Attendance_Rate", "GPA", "CGPA"]].describe())


# ================================================
# Program 3: Data Type Conversion
# ================================================
print("\n================================================")
print("Program 3: Data Type Conversion")
print("================================================")
sample_data = {"Roll": ["1", "2", "3", "4"]}
sample_df = pd.DataFrame(sample_data)
print("Before Conversion")
print(sample_df.dtypes)

sample_df["Roll"] = sample_df["Roll"].astype(int)
print("After Conversion")
print(sample_df.dtypes)


# ================================================
# Program 4: Exception Handling
# ================================================
print("\n================================================")
print("Program 4: Exception Handling")
print("================================================")
try:
    marks = int(input("Enter Marks: "))
    print("Marks =", marks)
except ValueError:
    print("Invalid Input")
finally:
    print("Program Completed")


# ================================================
# Program 5: Combined Program
# ================================================
print("\n================================================")
print("Program 5: Combined Program")
print("================================================")
print("Dataset Loaded Successfully")
print(df.describe())

try:
    df["Age"] = df["Age"].astype(float)
    print("Conversion Successful")
except Exception as e:
    print(e)