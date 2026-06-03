import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration setting up dashboard frame
st.set_page_config(page_title="Patient Readmission Analyzer", page_icon="🏥", layout="centered")

@st.cache_resource
def load_saved_pipeline_assets():
    try:
        model = joblib.load('healthcare_model.pkl')
        selector = joblib.load('healthcare_selector.pkl')
        return model, selector
    except FileNotFoundError:
        return None, None

model, selector = load_saved_pipeline_assets()

st.title("🏥 Patient 30-Day Readmission Risk Predictor")
st.markdown("""
This app evaluates vital sign metrics, demographics, and clinical measurements to calculate a patient's risk of being readmitted within a 30-day window.
""")
st.write("---")

if model is None or selector is None:
    st.error("⚠️ Pipeline binary model assets could not be located. Ensure 'healthcare_model.pkl' and 'healthcare_selector.pkl' exist in the workspace.")
else:
    # All base features available before SelectKBest step in training
    all_candidate_features = ['age', 'bmi', 'systolic_bp', 'cholesterol', 'length_of_stay_days', 'bp_bmi_ratio', 'is_senior', 'is_male']
    selected_indices = selector.get_support(indices=True)
    selected_features = [all_candidate_features[i] for i in selected_indices]

    st.subheader("📋 Step 1: Input Patient Vital Sign Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Patient Age:", min_value=1, max_value=120, value=45)
        gender = st.selectbox("Patient Gender Category:", options=["Female", "Male"])
        bmi = st.number_input("Body Mass Index (BMI Value):", min_value=10.0, max_value=60.0, value=25.4, step=0.1)

    with col2:
        systolic_bp = st.number_input("Systolic Blood Pressure (mmHg):", min_value=70, max_value=220, value=120)
        cholesterol = st.number_input("Serum Cholesterol Level (mg/dL):", min_value=100, max_value=400, value=195)
        length_of_stay = st.slider("Hospital Length of Stay Duration (Days):", min_value=1, max_value=30, value=3)

    # --- APP-SIDE DYNAMIC FEATURE ENGINEERING ---
    bp_bmi_ratio = systolic_bp / bmi if bmi > 0 else 0
    is_senior = 1 if age >= 65 else 0
    is_male = 1 if gender == "Male" else 0

    # Put feature entries into structured DataFrame row structure
    input_df = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'systolic_bp': systolic_bp,
        'cholesterol': cholesterol,
        'length_of_stay_days': length_of_stay,
        'bp_bmi_ratio': bp_bmi_ratio,
        'is_senior': is_senior,
        'is_male': is_male
    }])

    st.write("---")
    
    # 🚨 EVERYTHING BELOW HERE IS NOW PERFECTLY ALIGNED 🚨
    if st.button("Calculate Diagnostic Risk Inference", type="primary"):
        # 1. Isolate the features chosen by SelectKBest
        final_app_features = input_df[selected_features]
        
        # 2. Strip away names and pass pure numbers matrix
        pure_numbers = final_app_features.to_numpy()
        
        # 3. Safe prediction execution using the numbers matrix
        prediction = model.predict(pure_numbers)[0]
        probabilities = model.predict_proba(pure_numbers)[0]

        st.subheader("🎯 Classification Decision Output")
        if prediction == 1:
            st.error(f"⚠️ **High Risk: Patient is highly likely to be readmitted within 30 days.**")
            st.info(f"Model Confidence Score: {probabilities[1]*100:.2f}% probability of readmission.")
        else:
            st.success(f"✅ **Low Risk: Patient is unlikely to be readmitted within 30 days.**")
            st.info(f"Model Confidence Score: {probabilities[0]*100:.2f}% probability of staying healthy.")ilities[0]*100:.2f}% probability of staying healthy.")
