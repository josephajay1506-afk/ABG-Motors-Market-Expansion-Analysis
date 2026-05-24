# ==============================================
# ABG MOTORS CAPSTONE PROJECT
# Market Entry Analysis using Machine Learning
# ==============================================

# ==============================================
# IMPORT LIBRARIES
# ==============================================

import pandas as pd
import numpy as np

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==============================================
# STEP 1 — LOAD DATASETS
# ==============================================

print("Loading datasets...\n")

# Load CSV Files
jp = pd.read_csv("JPN Data.csv")
ind = pd.read_csv("IN Data.csv")

print("Japanese Dataset Loaded Successfully")
print("Indian Dataset Loaded Successfully\n")

# ==============================================
# STEP 2 — VIEW DATA
# ==============================================

print("Japanese Dataset Head:\n")
print(jp.head())

print("\nIndian Dataset Head:\n")
print(ind.head())

# ==============================================
# STEP 3 — DATA CLEANING
# ==============================================

print("\nCleaning Data...\n")

# Remove commas from income columns
jp['ANN_INCOME'] = jp['ANN_INCOME'].str.replace(',', '')
ind['ANN_INCOME'] = ind['ANN_INCOME'].str.replace(',', '')

# Convert income columns to float
jp['ANN_INCOME'] = jp['ANN_INCOME'].astype(float)
ind['ANN_INCOME'] = ind['ANN_INCOME'].astype(float)

# Encode Gender Column
jp['GENDER'] = jp['GENDER'].map({'M': 1, 'F': 0})
ind['GENDER'] = ind['GENDER'].map({'M': 1, 'F': 0})

# Fill Missing Values
jp.fillna(jp.mean(numeric_only=True), inplace=True)
ind.fillna(ind.mean(numeric_only=True), inplace=True)

print("Data Cleaning Completed\n")

# ==============================================
# STEP 4 — FEATURE SELECTION
# ==============================================

print("Selecting Features...\n")

# Input Features
X = jp[['CURR_AGE', 'GENDER', 'ANN_INCOME', 'AGE_CAR']]

# Target Variable
y = jp['PURCHASE']

# ==============================================
# STEP 5 — TRAIN TEST SPLIT
# ==============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Train-Test Split Completed\n")

# ==============================================
# STEP 6 — FEATURE SCALING
# ==============================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Feature Scaling Completed\n")

# ==============================================
# STEP 7 — BUILD LOGISTIC REGRESSION MODEL
# ==============================================

print("Training Logistic Regression Model...\n")

model = LogisticRegression()

model.fit(X_train, y_train)

print("Model Training Completed\n")

# ==============================================
# STEP 8 — MAKE PREDICTIONS
# ==============================================

y_pred = model.predict(X_test)

# ==============================================
# STEP 9 — MODEL EVALUATION
# ==============================================

print("===================================")
print("MODEL EVALUATION")
print("===================================\n")

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy Score:")
print(accuracy)

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n")
print(cm)

# ==============================================
# STEP 10 — MODEL COEFFICIENTS
# ==============================================

print("\n===================================")
print("MODEL COEFFICIENTS")
print("===================================\n")

coefficients = pd.DataFrame({
    'Feature': ['CURR_AGE', 'GENDER', 'ANN_INCOME', 'AGE_CAR'],
    'Coefficient': model.coef_[0]
})

print(coefficients)

# ==============================================
# STEP 11 — PREPARE INDIAN DATASET
# ==============================================

print("\nPreparing Indian Dataset for Prediction...\n")

# Create AGE_CAR column for Indian Dataset
ind['AGE_CAR'] = 5

# Select Features
X_ind = ind[['CURR_AGE', 'GENDER', 'ANN_INCOME', 'AGE_CAR']]

# Scale Data
X_ind = scaler.transform(X_ind)

# ==============================================
# STEP 12 — PREDICT INDIAN CUSTOMERS
# ==============================================

print("Predicting Potential Customers in Indian Market...\n")

ind_predictions = model.predict(X_ind)

# Add Prediction Column
ind['PREDICTED_PURCHASE'] = ind_predictions

# Count Potential Customers
potential_customers = ind_predictions.sum()

print("===================================")
print("INDIAN MARKET ANALYSIS")
print("===================================\n")

print("Total Potential Customers in Indian Market:")
print(potential_customers)

# ==============================================
# STEP 13 — SAVE OUTPUT FILES
# ==============================================

print("\nSaving Output Files...\n")

# Save Predictions
ind.to_csv("Indian_Market_Predictions.csv", index=False)

# Save Coefficients
coefficients.to_csv("Model_Coefficients.csv", index=False)

print("Files Saved Successfully\n")

print("Generated Files:")
print("1. Indian_Market_Predictions.csv")
print("2. Model_Coefficients.csv")

# ==============================================
# STEP 14 — FINAL BUSINESS CONCLUSION
# ==============================================

print("\n===================================")
print("FINAL BUSINESS CONCLUSION")
print("===================================\n")

if potential_customers >= 12000:
    print("The Indian market appears profitable for ABG Motors.")
    print("Predicted customer count exceeds the target of 12,000.")
else:
    print("The Indian market may not meet the expected target.")
    print("Further analysis is recommended.")

print("\nProject Completed Successfully!")