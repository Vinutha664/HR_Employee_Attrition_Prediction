import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("attrition_model.pkl","rb"))

st.title("HR Employee Attrition Prediction")

age = st.number_input("Age",18,60)
income = st.number_input("Monthly Income")
years = st.number_input("Years At Company")
satisfaction = st.slider("Job Satisfaction",1,4)
overtime = st.selectbox("OverTime",["Yes","No"])

overtime_value = 1 if overtime=="Yes" else 0

data = pd.DataFrame({
    "Age":[age],
    "MonthlyIncome":[income],
    "YearsAtCompany":[years],
    "JobSatisfaction":[satisfaction],
    "OverTime":[overtime_value]
})

if st.button("Predict Attrition"):
    prediction=model.predict(data)

    if prediction[0]==1:
        st.error("High Risk of Attrition")
    else:
        st.success("Low Risk of Attrition")
