# app.py
import streamlit as st
import numpy as np
import pickle


# Load model
with open("flight_price_prediction.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Price Prediction App", layout="centered")
st.title("🏠 Price Prediction App")
st.write("Enter the inputs below to predict the price:")

# --- Mappings for categorical fields (adjust to match your training encoding) ---
airline_map = {
    "IndiGo": 0,
    "Air India": 1,
    "SpiceJet": 2,
    "Vistara": 3,
    "GoAir": 4,
    "Multiple carriers": 5,
    "Air Asia": 6,
    "Other": 7
}

source_map = {
    "Delhi": 0,
    "Mumbai": 1,
    "Bengaluru": 2,
    "Chennai": 3,
    "Kolkata": 4,
    "Other": 5
}

destination_map = {
    "Mumbai": 0,
    "Delhi": 1,
    "Bengaluru": 2,
    "Chennai": 3,
    "Kolkata": 4,
    "Other": 5
}

stops_map = {
    "Non-stop": 0,
    "1 Stop": 1,
    "2 Stops": 2,
    "3+ Stops": 3
}

class_map = {
    "Economy": 0,
    "Premium Economy": 1,
    "Business": 2,
    "First": 3
}

# --- Input widgets ---
col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox("Airline", list(airline_map.keys()), index=0)
    source = st.selectbox("Source", list(source_map.keys()), index=0)
    destination = st.selectbox("Destination", list(destination_map.keys()), index=0)
    stops = st.selectbox("Stops", list(stops_map.keys()), index=1)

with col2:
    travel_class = st.selectbox("Class", list(class_map.keys()), index=0)
    duration_hours = st.number_input("Duration hours", min_value=0, max_value=48, value=2)
    duration_minutes = st.number_input("Duration minutes", min_value=0, max_value=59, value=30)
    day = st.number_input("Day of month", min_value=1, max_value=31, value=15)
    month = st.selectbox("Month", ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], index=7)

# Convert month name to number
month_map = {m:i+1 for i,m in enumerate(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])}
month_num = month_map[month]

# Build numeric feature vector (9 columns)
features = [
    airline_map.get(airline, airline_map["Other"]),
    source_map.get(source, source_map["Other"]),
    destination_map.get(destination, destination_map["Other"]),
    stops_map.get(stops, 3),
    class_map.get(travel_class, 0),
    float(duration_hours),
    float(duration_minutes),
    int(day),
    int(month_num)
]

st.write("Input vector (order: Airline, Source, Destination, Stops, Class, Duration_hours, Duration_minutes, Day, Month):")
st.write(np.array(features))

# Predict button
if st.button("Predict Price 💰"):
    X = np.array([features])
    try:
        prediction = model.predict(X)[0]
        st.success(f"Predicted Price: ₹ {prediction:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed. Model may expect a different feature encoding/shape.\nError: {e}")
# ...existing code...

