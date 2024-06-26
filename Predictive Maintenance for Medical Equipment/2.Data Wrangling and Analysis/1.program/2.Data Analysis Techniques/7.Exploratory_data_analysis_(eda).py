import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = """Equipment ID,Date,Sensor 1 (Temperature),Sensor 2 (Pressure),Sensor 3 (Vibration),Maintenance History,Failure
1,2022-01-01 08:00:00,28.5,102.3,0.8,None,0
2,2022-01-01 08:15:00,30.2,98.7,1.2,Maintenance 1,0
3,2022-01-01 08:30:00,27.8,99.9,1.0,None,0
4,2022-01-01 08:45:00,29.3,100.5,0.9,Maintenance 2,0
5,2022-01-01 09:00:00,31.0,97.6,1.5,None,1"""

# Check the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Data visualization

# Distribution of Sensor readings
plt.figure(figsize=(10, 6))
sns.histplot(df['Sensor 1 (Temperature)'], bins=20, color='blue', kde=True)
plt.title('Distribution of Temperature')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Sensor 2 (Pressure)'], bins=20, color='green', kde=True)
plt.title('Distribution of Pressure')
plt.xlabel('Pressure')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Sensor 3 (Vibration)'], bins=20, color='orange', kde=True)
plt.title('Distribution of Vibration')
plt.xlabel('Vibration')
plt.ylabel('Frequency')
plt.show()

# Pairplot for Sensor readings
print("\nPairplot for Sensor readings:")
sns.pairplot(df[['Sensor 1 (Temperature)', 'Sensor 2 (Pressure)', 'Sensor 3 (Vibration)']])
plt.show()

# Relationship between Maintenance History and Failure
print("\nRelationship between Maintenance History and Failure:")
sns.countplot(x='Maintenance History', hue='Failure', data=df)
plt.title('Maintenance History vs Failure')
plt.xlabel('Maintenance History')
plt.ylabel('Count')
plt.show()