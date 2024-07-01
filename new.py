import pandas as pd
from flask import Flask, render_template, jsonify, request
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

@app.route('/')
def home():
    return render_template('home.html')

# Read the dataset
df = pd.read_csv('RISKK.csv')

# Preprocess the data
scaler = MinMaxScaler()
df[['EPI', 'UDI', 'LUV', 'CRI']] = scaler.fit_transform(df[['EPI', 'UDI', 'LUV', 'CRI']])

# Calculate correlation matrix with the assumption that RISK_FACTOR exists in the dataset
correlation_matrix = df[['EPI', 'UDI', 'LUV', 'CRI', 'RISK_FACTOR']].corr()['RISK_FACTOR'].drop('RISK_FACTOR')

# Assign weights based on correlation values
weights = correlation_matrix.abs() / correlation_matrix.abs().sum()

# Calculate the risk factor using weighted sum
def calculate_risk_factor(row):
    return (row['EPI'] * weights['EPI'] +
            row['UDI'] * weights['UDI'] +
            row['LUV'] * weights['LUV'] +
            row['CRI'] * weights['CRI'])

df['RISK_FACTOR'] = df.apply(calculate_risk_factor, axis=1)

# Ensure the risk factor is within the range 0 to 1
df['RISK_FACTOR'] = df['RISK_FACTOR'].clip(lower=0, upper=1)

# Define risk clusters
def classify_risk(risk):
    if risk < 0.25:
        return 'Very Good'
    elif 0.25 <= risk < 0.4:
        return 'Good'
    elif 0.4 <= risk < 0.55:
        return 'Moderate'
    elif 0.55 <= risk < 0.65:
        return 'Bad'
    else:
        return 'Very Bad'

# Map risk factor to risk classification
df['CLUSTER'] = df['RISK_FACTOR'].apply(classify_risk)

# Encode categorical variables
label_encoder = LabelEncoder()
df['CLUSTER'] = label_encoder.fit_transform(df['CLUSTER'])

# Select features and target variable
X = df[['EPI', 'UDI', 'LUV', 'CRI']]
y = df['CLUSTER']

# Train Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Predict risk classification for all areas
y_pred = model.predict(X)

# Add predicted risk classification to the DataFrame
df['PREDICTED_CLUSTER'] = label_encoder.inverse_transform(y_pred)

# Display the DataFrame with the predicted risk classifications
print("All Predicted Values:")
for area, predicted_cluster in zip(df['Areas'], df['PREDICTED_CLUSTER']):
    print(f"{area}: {predicted_cluster}")

# Evaluate the model
print("\nClassification Report:")
print(classification_report(y, y_pred, target_names=label_encoder.classes_))

def predict_risk_classification(epi, udi, luv, cri):
    # Scale the input values using the same scaler
    scaled_values = scaler.transform([[epi, udi, luv, cri]])

    # Create a DataFrame from the scaled values
    input_df = pd.DataFrame(scaled_values, columns=['EPI', 'UDI', 'LUV', 'CRI'])

    # Calculate the risk factor
    risk_factor = calculate_risk_factor(input_df.iloc[0])

    # Adjust risk factor if it is out of bounds
    if risk_factor > 1:
        risk_factor = 0.9
    elif risk_factor < 0:
        risk_factor = 0.1

    # Classify the risk factor
    risk_class = classify_risk(risk_factor)

    # Encode the classified risk
    encoded_risk_class = label_encoder.transform([risk_class])[0]

    # Predict the risk cluster using the model
    predicted_cluster = model.predict(input_df)[0]

    # Decode the predicted cluster
    predicted_cluster_decoded = label_encoder.inverse_transform([predicted_cluster])[0]

    return risk_factor, predicted_cluster_decoded

# Example usage: Take user input for EPI, UDI, LUV, and CRI
user_epi = float(input("Enter EPI: "))
user_udi = float(input("Enter UDI: "))
user_luv = float(input("Enter LUV: "))
user_cri = float(input("Enter CRI: "))

# Predict the risk factor and cluster
risk_factor, predicted_cluster = predict_risk_classification(user_epi, user_udi, user_luv, user_cri)

# Display the results
print(f"\nRisk Factor: {risk_factor}")
print(f"Predicted Risk Classification: {predicted_cluster}")