# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 12:32:51 2025

@author: abc
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/abc/Desktop/ML models/trained_model.sav','rb'))

#creating function for prediction
def diabetes_prediction(input_data):
    
    #converting input data as numpy array
    input_as_numpy_array = np.asarray(input_data)

    #reshaping input as we are prediciting for one instance only
    input_reshaped = input_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_reshaped)

    if (prediction[0] == 0):
      return 'Person is non diabetic'
    else:
      return 'Person is diabetic'
  
    
  
def main():
    
    #giving title to web page
    st.title('Diabetes Prediction App')
    
    #Taking Input for different values
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Thickness of Skin')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('Body Mass Index(BMI)')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of Patient')
    
    
    #code for prediction
    diagnosis = ''
    
    #creating a button
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()

    
    
    
    
    
    