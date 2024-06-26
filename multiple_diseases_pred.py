# -*- coding: utf-8 -*-
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Diagnose AI",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Get the directory where this script is located
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved models/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved models/heart_model.sav','rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved models/parkinsons_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Diagnose AI',['Diabetes','Heart Disease',"Parkinson's Disease"],
                           icons=['activity','heart','person'],
                           default_index = 0)


# Diabetes Prediction Page
if(selected == 'Diabetes'):
    st.title("Diabetes Prediction using ML")
    
    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Level")
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    with col2:
        Age = st.text_input("Patient's Age")
    
    # code for prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    if st.button("Diabetes Test Result"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if(diab_prediction[0] == 0):
            diab_diagnosis = "Patient is Not Diabetic"
        else:
            diab_diagnosis = "Patient is Diabetic"
    st.success(diab_diagnosis)
    
if(selected=='Heart Disease'):
    st.title("Heart Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Patient's Age")
    with col2:
        sex = st.text_input("Patient's Sex")
    with col3:
        cp = st.text_input("Chest Pain Type")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic")
    with col2:
        thalach = st.text_input("Max Heart Rate")
    with col3:
        exang = st.text_input("Exercise-Induced Angina")
    with col1:
        oldpeak = st.text_input("ST Depression Induced by Exercise")
    with col2:
        slope = st.text_input("Slope of Peak Exercise ST Segment")
    with col3:
        ca = st.text_input("Number of Major Vessels (0-3)")
    thal = st.text_input("Thalassemia - 0 = normal, 1 = fixed defect, 2 = reversable defect")
    
    hd_diagnosis = ''
    if st.button("Heart Disease Test Result"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        hd_prediction = heart_disease_model.predict([user_input])
        if(hd_prediction[0] == 0):
            hd_diagnosis = "Patient does Not Have Heart Disease"
        else:
            hd_diagnosis = "Patient Has Heart Disease"
    st.success(hd_diagnosis)
        
    
if(selected=="Parkinson's Disease"):
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4= st.columns(4)
    
    with col1:
        fo = st.text_input("MDVP Fo in Hz")
    with col2:
        fhi = st.text_input("MDVP Fhi in Hz")
    with col3:
        flo = st.text_input("MDVP Flo in Hz")
    with col4:
        Jitter_P = st.text_input("MDVP Jitter in %")
    with col1:
        Jitter_Abs = st.text_input("MDVP Jitter in Abs")
    with col2:
        RAP = st.text_input("MDVP RAP")
    with col3:
        PPQ = st.text_input("MDVP PPQ")
    with col4:
        Jitter_DDP = st.text_input("Jitter DDP")
    with col1:
        Shimmer = st.text_input("MDVP Shimmer")
    with col2:
        Shimmer_dB = st.text_input("MDVP Shimmer dB")
    with col3:
        Shimmer_APQ3 = st.text_input("Shimmer APQ3")
    with col4:
        Shimmer_APQ5 = st.text_input("Shimmer APQ5")
    with col1:
        APQ = st.text_input("MDVP APQ")
    with col2:
        Shimmer_DDA = st.text_input("Shimmer DDA")
    with col3:
        NHR = st.text_input("NHR")
    with col4:
        HNR = st.text_input("HNR")
    with col1:
        status = st.text_input("status")
    with col2:
        RDPE = st.text_input("RDPE")
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("spread1")
    with col1:
        spread2 = st.text_input("spread2")
    with col2:
        D2 = st.text_input("D2")
    with col3:
        PPE = st.text_input("PPE")
        
    pd_diagnosis = ''
    if st.button("Parkinson's Disease Test Result"):
        user_input = [fo,fhi,flo,Jitter_P,Jitter_Abs,RAP,
                      PPQ,Jitter_DDP,Shimmer,Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,
                      APQ,Shimmer_DDA,NHR,HNR,RDPE,DFA,spread1,spread2,D2,PPE]
        user_input = [float(x) for x in user_input]
        pd_prediction = parkinsons_model.predict([user_input])
        if(pd_prediction[0] == 0):
            pd_diagnosis = "Patient does Not Have Parkinson's Disease"
        else:
            pd_diagnosis = "Patient Has Parkinson's Disease"
    st.success(pd_diagnosis)
