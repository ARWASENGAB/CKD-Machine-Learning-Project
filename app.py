
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("ckd_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.title("Chronic Kidney Disease Prediction App")
st.write("Enter patient clinical values to predict CKD status.")

input_data = {}

for feature in features:
    input_data[feature] = st.number_input(f"Enter {feature}", value=0.0)

input_df = pd.DataFrame([input_data])
input_scaled = scaler.transform(input_df)

prediction = model.predict(input_scaled)[0]

st.subheader("Prediction Result")

if prediction == 1:
    st.error("The patient is predicted to have Chronic Kidney Disease.")
else:
    st.success("The patient is predicted to NOT have Chronic Kidney Disease.")
