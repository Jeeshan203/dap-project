import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif

df = pd.read_csv("student_dropout_dataset_v3.csv")

numeric_columns = ["Age", "Family_Income", "Study_Hours_per_Day", "Attendance_Rate",
                    "Assignment_Delay_Days", "Travel_Time_Minutes", "Stress_Index",
                    "GPA", "Semester_GPA", "CGPA"]

df[numeric_columns] = df[numeric_columns].fillna(0)

X = df[numeric_columns]
y = df["Dropout"]

# ================================================
# Program 1: Correlation Analysis
# ================================================
print("Correlation Matrix")
print(X.corr())

sns.heatmap(X.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# ================================================
# Program 2: Variance Threshold
# ================================================
print("\n================================================")
print("Program 2: Variance Threshold")
print("================================================")
selector_var = VarianceThreshold(threshold=0.2)
X_var = selector_var.fit_transform(X)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_var.shape)
print("Selected Features:", selector_var.get_support())

# ================================================
# Program 3: Univariate Feature Selection
# ================================================
print("\n================================================")
print("Program 3: Univariate Feature Selection")
print("================================================")
selector_uni = SelectKBest(score_func=f_classif, k=2)
X_new = selector_uni.fit_transform(X, y)

print("Scores:", selector_uni.scores_)
print("Selected Features:", selector_uni.get_support())

# ================================================
# Program 4: Feature Ranking
# ================================================
print("\n================================================")
print("Program 4: Feature Ranking")
print("================================================")
selector_all = SelectKBest(f_classif, k="all")
selector_all.fit(X, y)

ranking = pd.DataFrame({
    "Feature": X.columns,
    "Score": selector_all.scores_
})
ranking = ranking.sort_values(by="Score", ascending=False)
print(ranking.to_string(index=False))

# ================================================
# Program 5: Complete Feature Selection
# ================================================
print("\n================================================")
print("Program 5: Complete Feature Selection")
print("================================================")
selector_var2 = VarianceThreshold(0.2)
X_var2 = selector_var2.fit_transform(X)

selector_best = SelectKBest(f_classif, k=2)
X_best = selector_best.fit_transform(X_var2, y)

print("Shape after Variance Threshold:", X_var2.shape)
print("Shape after Feature Selection:", X_best.shape)
print("Feature Scores:", selector_best.scores_)