import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("student_performance_unclean.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display dataset information
print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Check unique values in Gender
print("\nGender Values:")
print(df["Gender"].unique())

# Check unique values in Department
print("\nDepartment Values:")
print(df["Department"].unique())
