import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3.csv")

# ================================================
# Program 1: Loading the Dataset
# ================================================
print("Total Records:", len(df))
print(df)

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
print("Before Conversion")
print(df["Family_Income"].dtype)

df["Family_Income"] = df["Family_Income"].fillna(0)
df["Family_Income"] = df["Family_Income"].astype(int)

print("After Conversion")
print(df["Family_Income"].dtype)
print(df["Family_Income"])

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