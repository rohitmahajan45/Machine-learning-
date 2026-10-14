import streamlit as st
import numpy as np
import joblib

model=joblib.load('Data.joblib')

# page title
st.title("prediction")

# input value
cgpa=st.number_input("enter cgpa")

if st.button("predict package"):
    try:
        input_data=np.array([[cgpa]])
        
        prediction=model.predict(input_data)
        
        st.success(prediction)
    except Exception as e:
        print(e)
        