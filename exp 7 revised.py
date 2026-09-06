import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3.csv")

# ================================================
# Program 1: Load the Dataset
# ================================================
print("Total Records:", len(df))
print(df)

# ================================================
# Program 2: Handling Missing Values
# ================================================
print("\n================================================")
print("Program 2: Handling Missing Values")
print("================================================")
print("Missing Values in Each Column")
print(df.isnull().sum())

df["Family_Income"] = df["Family_Income"].fillna(0)
df["Study_Hours_per_Day"] = df["Study_Hours_per_Day"].fillna(0)
df["Stress_Index"] = df["Stress_Index"].fillna(0)
df["Parental_Education"] = df["Parental_Education"].fillna("Not Known")

print("Missing Values After Filling")
print(df.isnull().sum())

# ================================================
# Program 3: Removing Duplicate Records
# ================================================
print("\n================================================")
print("Program 3: Removing Duplicate Records")
print("================================================")
print("Duplicate Records Before Removing:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate Records After Removing:", df.duplicated().sum())
print("Dataset Shape After Removing Duplicates:", df.shape)

# ================================================
# Program 4: Basic Data Filtering
# ================================================
print("\n================================================")
print("Program 4: Basic Data Filtering")
print("================================================")
filtered = df[df["GPA"] >= 3.0]
print("Number of Students with GPA 3.0 or above:", len(filtered))
print(filtered)

# ================================================
# Program 5: Complete Data Cleaning
# ================================================
print("\n================================================")
print("Program 5: Complete Data Cleaning")
print("================================================")
print("Final Cleaned Dataset Shape:", df.shape)

dropout_students = df[df["Dropout"] == 1]
print("Number of Students Who Dropped Out:", len(dropout_students))
print(dropout_students)