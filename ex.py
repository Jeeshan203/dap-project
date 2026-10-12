import matplotlib.pyplot as plt

from main import df

# 1. Get the value counts from your dataframe
department_counts = df["Department"].value_counts()

# 2. Initialize the plot figure
plt.figure(figsize=(8, 5))

# 3. Create the bar chart
plt.bar(department_counts.index, department_counts.values, color="orange")

# 4. Add titles and labels
plt.title("Department Wise Student Count")
plt.xlabel("Department")
plt.ylabel("Number of Students")

# 5. Display the graph
plt.show()
