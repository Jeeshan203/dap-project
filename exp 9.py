import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("student_dropout_dataset_v3.csv")

numeric_columns = ["Age", "Family_Income", "Study_Hours_per_Day", "Attendance_Rate",
                    "Assignment_Delay_Days", "Travel_Time_Minutes", "Stress_Index",
                    "GPA", "Semester_GPA", "CGPA"]

df[numeric_columns] = df[numeric_columns].fillna(0)

# ================================================
# Program 1: Create a Histogram
# ================================================
plt.figure(figsize=(6, 4))
plt.hist(df["GPA"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of GPA")
plt.xlabel("GPA")
plt.ylabel("Frequency")
plt.show()

# ================================================
# Program 2: Compute a Correlation Matrix
# ================================================
correlation_matrix = df[numeric_columns].corr()
print(correlation_matrix)

# ================================================
# Program 3: Create a Correlation Heatmap
# ================================================
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# ================================================
# Program 4: Create a Pair Plot
# ================================================
sample_df = df[numeric_columns + ["Dropout"]].sample(n=300, random_state=1)
sns.pairplot(sample_df, hue="Dropout")
plt.show()

# ================================================
# Program 5: Create a Box Plot Using Seaborn
# ================================================
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[numeric_columns])
plt.xticks(rotation=45)
plt.title("Box Plot of Numerical Features")
plt.show()