# @title
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load the dataset
data = '/content/sample_data/pm-data set.csv'


# Temporal Analysis
df['Date'] = pd.to_datetime(df['Date'])
df['hour_of_day'] = df['Date'].dt.hour

# User Profiles (Mean sensor readings for each equipment)
user_profiles = df.groupby('Equipment ID').agg({
    'Sensor 1 (Temperature)': 'mean',
    'Sensor 2 (Pressure)': 'mean',
    'Sensor 3 (Vibration)': 'mean'
}).reset_index()

# Content Embeddings (One-hot encoding for 'Maintenance History')
maintenance_encoder = OneHotEncoder()
maintenance_encoded = maintenance_encoder.fit_transform(df[['Maintenance History']])

# Print the modified DataFrame and user profiles
print("Modified DataFrame:")
print(df)
print("\nmechin Profil:")
print(user_profiles)
print("\nOne-hot Encoded Maintenance History:")
print(maintenance_encoded.toarray())