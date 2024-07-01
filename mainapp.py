from flask import Flask, render_template, jsonify, request
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

import pickle

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return render_template('home.html')


# Read the dataset
df = pd.read_csv('RISKK.csv')

# Preprocess the data
scaler = MinMaxScaler()
df[['EPI', 'UDI', 'LUV', 'CRI']] = scaler.fit_transform(df[['EPI', 'UDI', 'LUV', 'CRI']])

# Calculate correlation matrix
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

# Define risk clusters
def classify_risk(risk):
    if risk < 0.25:
        return 'Very Good'
    elif 0.25 < risk < 0.4:
        return 'Good'
    elif 0.4 < risk < 0.55:
        return 'Moderate'
    elif 0.55 < risk < 0.65:
        return 'Bad'
    elif risk >= 0.65:
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
    print(f"{area}: {predicted_cluster} ")

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
        risk_factor = 0.9998
    elif risk_factor < 0:
        risk_factor = 0.545

    # Classify the risk factor
    risk_class = classify_risk(risk_factor)

    # Encode the classified risk
    encoded_risk_class = label_encoder.transform([risk_class])[0]

    # Predict the risk cluster using the model
    predicted_cluster = model.predict(input_df)[0]

    # Decode the predicted cluster
    predicted_cluster_decoded = label_encoder.inverse_transform([predicted_cluster])[0]

    return risk_factor, predicted_cluster_decoded

@app.route('/real')
def new_pager():
    return render_template('realtempereature.html')

@app.route('/calculate_indices', methods=['GET'])
def calculate_indices():
    # Load the CSV files
    ntl = pd.read_csv('NTL_Katraj (1).csv')
    ndvi = pd.read_csv('ndvi_katraj_time.csv')
    realtime = pd.read_csv('practisef.csv')

    # Calculate averages for environmental components
    b_co_avg = realtime['CO2(PPM)'].max()
    c_so2_avg = realtime['SO2(PPM)'].max()
    d_aod_avg = realtime['DUST DENSITY(UG/M3)'].max()

    # Calculate medians for environmental components (optional, for use if median is preferred)
    b_co_median = realtime['CO2(PPM)'].median()
    c_so2_median = realtime['SO2(PPM)'].median()
    d_aod_median = realtime['DUST DENSITY(UG/M3)'].median()

    # Choose either average or median for EPI calculation
    # Here using average
    epi = (b_co_avg + c_so2_avg + d_aod_avg) / 4

    # Correctly handle the 'urban' column in ntl DataFrame
    ntl['urban'] = (ntl['urban'].str.replace(',', '').astype(float))
    udi = ntl['urban'].median() / 2

    # Correctly handle the '0' column in ndvi DataFrame if it has commas (if needed)
    # ndvi['0'] = ndvi['0'].str.replace(',', '').astype(float)  # Uncomment if necessary
    luv = ndvi['0'].median() / 2

    # Use average for CRI calculation
    temperature_avg = realtime['TEMPERATURE(CELCIUS)'].max()
    humidity_avg = realtime['HUMIDITY(%)'].max()

    cri = (temperature_avg + humidity_avg) / 4

    # Combine all indices into a single DataFrame
    main_indices = pd.DataFrame({
        'EPI': [epi],
        'UDI': [udi],
        'LUV': [luv],
        'CRI': [cri]
    })

    # Save the new dataset
    main_indices.to_csv('main_indices.csv', index=False)

    response = {
        'b_co_avg': b_co_avg,
        'c_so2_avg': c_so2_avg,
        'd_aod_avg': d_aod_avg,
        'temperature_avg': temperature_avg,
        'humidity_avg': humidity_avg,
        'ntl_avg': ntl['urban'].mean()  # Added ntl_avg calculation
    }

    return jsonify(response)

@app.route('/calculate_risk', methods=['POST'])
def calculate_risk():
    data = pd.read_csv("main_indices.csv")
    epi = data['EPI'][0]
    udi = data['UDI'][0]
    luv = data['LUV'][0]
    cri = data['CRI'][0]

    risk_factor, predicted_cluster = predict_risk_classification(epi, udi, luv, cri)

    #import google.generativeai as genai

    #api_key = 'YOUR_API_KEY_HERE'
    #genai.configure(api_key='AIzaSyDKLst8XnQhcOxYWYVeiI5KnySRc8IY3YU')

    #model = genai.GenerativeModel(model_name="gemini-pro")
    #prompt_parts = ["Tell me about katraj city in 100 words focus on whether it is livable or not?"]
    #response = model.generate_content(prompt_parts)

    #return response.text
    response = {
        'epi' : epi,
        'udi' : udi,
        'luv' : luv,
        'cri' : cri,
        'risk_factor': risk_factor,
        'predicted_cluster': predicted_cluster,
        #'responsetext' : response.txt
    }

    return jsonify(response)

@app.route('/risk')
def new_page():
    return render_template('risk.html')

if __name__ == '__main__':
    app.run(debug=True)
