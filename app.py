import os
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

api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    st.error('GEMINI_API_KEY not found. Please export it as an environment variable or add it in the .env file')

symptom_checker = SymptomChecker(api_key)

if submit:
    st.write(symptom_checker.get_response(symptoms))