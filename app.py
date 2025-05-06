import streamlit as st
from symptom_checker import SymptomChecker

st.set_page_config(page_title='Symptom Checker')
st.subheader('Symptom Checker and Specialist Recommender')

symptoms = st.text_area('Please write your symptoms here:', key='input')
submit = st.button('Ask for recommendations')

symptom_checker = SymptomChecker()

if submit:
    st.write(symptom_checker.get_response(symptoms))