
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('employees.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Display basic information about the dataset
print("\nBasic information about the dataset:")
print(df.info())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nCheck for missing values:")
print(df.isnull().sum())

# Plot histograms
print("\nHistograms:")
df.hist(figsize=(10, 8))
plt.show()

# Box plots
print("\nBox plots:")
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.show()

# Pair plot
print("\nPair plot:")
sns.pairplot(df)
plt.show()

# Heatmap
print("\nHeatmap:")
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Group by Department and calculate mean of each feature
print("\nMean values by Department:")
print(df.groupby('Department').mean())

# Salary distribution by Department
print("\nSalary distribution by Department:")
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Salary', data=df)
plt.title('Salary Distribution by Department')
plt.show()

# Years of Experience distribution by Department
print("\nYears of Experience distribution by Department:")
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Years_Experience', data=df)
plt.title('Years of Experience Distribution by Department')
plt.show()

# Salary vs Years of Experience
print("\nSalary vs Years of Experience:")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years_Experience', y='Salary', hue='Department', data=df)
plt.title('Salary vs Years of Experience')
plt.show()
