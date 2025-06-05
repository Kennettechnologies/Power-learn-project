# model_dev.py
# Model Development Script

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load preprocessed data
# data = pd.read_csv('preprocessed_data.csv')
# X = data.drop('target', axis=1)
# y = data['target']

# Split data
# X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

# Train model
# model = LogisticRegression()
# model.fit(X_train, y_train)

# Save model
# joblib.dump(model, 'logistic_model.pkl') 