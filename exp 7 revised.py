import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3.csv")

# ================================================
# Program 1: Load the Dataset
# ================================================
print(df.head())

# ================================================
# Program 2: Handling Missing Values
# ================================================
print("\n================================================")
print("Program 2: Handling Missing Values")
print("================================================")
print("Missing Values in Each Column")
print(df.isnull().sum())

income_filled = df["Family_Income"].fillna(0)
print("Family Income After Filling Missing Values")
print(income_filled.head(10))

# ================================================
# Program 3: Removing Duplicate Records
# ================================================
print("\n================================================")
print("Program 3: Removing Duplicate Records")
print("================================================")
sample_df = df[["Student_ID", "Age", "GPA"]].head(5)
sample_df = pd.concat([sample_df, sample_df.tail(1)], ignore_index=True)
print("Sample Data with a Repeated Row")
print(sample_df)
print("After Removing Duplicates")
print(sample_df.drop_duplicates())

# ================================================
# Program 4: Basic Data Filtering
# ================================================
print("\n================================================")
print("Program 4: Basic Data Filtering")
print("================================================")
filtered = df[df["GPA"] >= 3.0]
print("Students with GPA 3.0 or above")
print(filtered.head())

# ================================================
# Program 5: Complete Data Cleaning
# ================================================
print("\n================================================")
print("Program 5: Complete Data Cleaning")
print("================================================")
print("Original Dataset Shape")
print(df.shape)

clean_df = df.copy()
clean_df["Family_Income"] = clean_df["Family_Income"].fillna(0)
clean_df["Study_Hours_per_Day"] = clean_df["Study_Hours_per_Day"].fillna(0)
clean_df["Stress_Index"] = clean_df["Stress_Index"].fillna(0)
clean_df["Parental_Education"] = clean_df["Parental_Education"].fillna("Not Known")

clean_df = clean_df.drop_duplicates()

print("Cleaned Dataset Shape")
print(clean_df.shape)

print("Students Who Dropped Out")
print(clean_df[clean_df["Dropout"] == 1].head())