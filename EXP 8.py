import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3.csv")

# ================================================
# Program 1: Exploratory Data Analysis Using Pandas
# ================================================
print("First Five Records")
print(df.head())

print("\nLast Five Records")
print(df.tail())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values in Each Column")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

print("\nDepartment Wise Frequency")
print(df["Department"].value_counts())

# ================================================
# Program 2: Line Plot Using Matplotlib
# ================================================
plt.figure(figsize=(8, 5))
plt.plot(df["GPA"])
plt.title("GPA Across All Students")
plt.xlabel("Student Index")
plt.ylabel("GPA")
plt.show()

# ================================================
# Program 3: Bar Chart Using Matplotlib
# ================================================
department_counts = df["Department"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(department_counts.index, department_counts.values, color="orange")
plt.title("Department Wise Student Count")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.show()