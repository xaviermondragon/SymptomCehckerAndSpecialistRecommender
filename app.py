import streamlit as st
from symptom_checker import SymptomChecker

invitation_text = \
'''
Hi, I'm your artificial intelligence based medical assistant. \
Please write your symptoms and I will give you appropriate recommendations. \
Click the "Ask for recommendations" button when you have finished writing your symptoms.
'''

st.set_page_config(page_title='Symptom Checker')
st.subheader('Symptom Checker and Specialist Recommender')

symptoms = st.text_area(invitation_text, key='input')
submit = st.button('Ask for recommendations')

symptom_checker = SymptomChecker()

if submit:
    #st.write(symptom_checker.get_symptoms(symptoms))
    st.write(symptom_checker.get_response(symptoms))