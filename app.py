import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('rainfall_prediction_model.pkl')

st.set_page_config(page_title="🌧️ Rainfall Prediction App", layout="centered")
st.title("🌧️ Rainfall Prediction System")
st.write("Enter the weather details to predict whether it will rain or not:")

# User inputs (replace these fields if your model uses different ones)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=150.0, step=0.1)
pressure = st.number_input("Pressure (hPa)", min_value=800.0, max_value=1100.0, step=0.1)

# Create DataFrame for prediction
input_data = pd.DataFrame({
    'Temperature': [temperature],
    'Humidity': [humidity],
    'WindSpeed': [wind_speed],
    'Pressure': [pressure]
})

# Predict on button click
if st.button("Predict Rainfall"):
    prediction = model['model'].predict(input_data)

    if prediction[0] == 1:
        st.success("🌧️ Rain is expected.")
    else:
        st.info("☀️ No rain expected.")
