import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (assuming 'data_preprocessed_df' from previous steps)
# data = pd.read_csv('your_data.csv')  # Uncomment if you load the original data.

# 2.2 (a) Exploratory Data Analysis (EDA)

# 1. Compute basic statistics
print("Basic Statistics:")
print(data_preprocessed_df.describe())  # Mean, Median, Standard Deviation, etc.

# 2. Check for data types and null values
print("\nData Information (Info):")
print(data_preprocessed_df.info())

# 3. Compute correlations
# Check for correlations between numeric columns using Pearson's correlation
correlation_matrix = data_preprocessed_df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Identify correlations visually via a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# 4. Check for outliers using box plots
plt.figure(figsize=(10, 6))
sns.boxplot(data=data_preprocessed_df)
plt.title("Boxplot to Identify Outliers")
plt.xticks(rotation=90)
plt.show()

# 5. Check for data imbalances (e.g., for a target variable in a classification problem)
# Assuming you have a target column, like 'target_column'
if 'target_column' in data_preprocessed_df.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(x='target_column', data=data_preprocessed_df)
    plt.title('Class Distribution of Target Variable')
    plt.show()

# 2.2 (b) Data Visualization
# Visualizing the distribution of a numeric feature
plt.figure(figsize=(8, 6))
sns.histplot(data_preprocessed_df['feature_column'], kde=True, color='skyblue')
plt.title('Distribution of Feature Column')
plt.xlabel('Feature Column')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to explore relationships between two numeric features
plt.figure(figsize=(8, 6))
sns.scatterplot(x='feature_column_1', y='feature_column_2', data=data_preprocessed_df)
plt.title('Scatter Plot: Feature Column 1 vs Feature Column 2')
plt.xlabel('Feature Column 1')
plt.ylabel('Feature Column 2')
plt.show()

# Box plot to visualize the distribution of a numeric feature across categories (if applicable)
# Assuming 'category_column' is a categorical feature
if 'category_column' in data_preprocessed_df.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='category_column', y='feature_column_1', data=data_preprocessed_df)
    plt.title('Box Plot: Feature Column 1 by Category')
    plt.show()
