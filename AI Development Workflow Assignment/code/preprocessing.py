# preprocessing.py
# Data Preprocessing Script

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load data (replace 'data.csv' with your actual data file)
data = pd.read_csv('data.csv')

# Handle missing values
# Example: data = data.fillna(method='ffill')

# Normalize numerical features
# scaler = StandardScaler()
# data[['num_feature1', 'num_feature2']] = scaler.fit_transform(data[['num_feature1', 'num_feature2']])

# Encode categorical variables
# encoder = OneHotEncoder(sparse=False)
# cat_encoded = encoder.fit_transform(data[['cat_feature']])

# Save preprocessed data
# data.to_csv('preprocessed_data.csv', index=False) 