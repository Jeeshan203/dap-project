import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

df = pd.read_csv("student_dropout_dataset_v3.csv")

# Select two numerical features
df_clean = df[["GPA", "Attendance_Rate"]].dropna()
X = df_clean.to_numpy()

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot original data points
plt.figure(figsize=(7, 6))
plt.scatter(X[:, 0], X[:, 1], color="blue", alpha=0.3, s=10)

# Mean point of the data
mean = np.mean(X, axis=0)

# First principal component direction
vector = pca.components_[0]

# Draw principal component arrow
plt.quiver(
    mean[0], mean[1],
    vector[0], vector[1],
    color="red", scale=2, width=0.01
)

plt.xlabel("GPA")
plt.ylabel("Attendance Rate")
plt.title("Principal Component Analysis")
plt.grid(True)
plt.show()

print("Principal Components")
print(pca.components_)

print("\nExplained Variance Ratio")
print(pca.explained_variance_ratio_)