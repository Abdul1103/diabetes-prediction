# app.py
import streamlit as st
import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).parent / 'model' / 'diabetes_model.pkl'
model = joblib.load(MODEL_PATH)

st.title("🩺 Diabetes Prediction Demo")
st.write("Enter the patient's health details:")

pregnancies = st.number_input("Pregnancies", min_value=0, step=1, value=0)
glucose = st.number_input("Glucose", min_value=0.0, value=120.0)
bp = st.number_input("Blood Pressure", min_value=0.0, value=70.0)
skin = st.number_input("Skin Thickness", min_value=0.0, value=20.0)
insulin = st.number_input("Insulin", min_value=0.0, value=79.0)
bmi = st.number_input("BMI", min_value=0.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.5)
age = st.number_input("Age", min_value=1, value=33)

if st.button("Predict"):
    X = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1] if hasattr(model, 'predict_proba') else None
    if pred == 1:
        if proba is not None:
            st.error(f"🔴 Diabetes detected — probability {proba:.2f}")
        else:
            st.error("🔴 Diabetes detected")
    else:
        if proba is not None:
            st.success(f"🟢 No diabetes — probability {proba:.2f}")
        else:
            st.success("🟢 No diabetes detected")