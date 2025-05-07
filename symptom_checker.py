import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from healthcare_advice import HealthcareAdvice

load_dotenv()

class SymptomChecker:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
        #self.chat = self.client.chats.create(model='gemini-2.0-flash', history=[])

    #def get_symptoms(self, input_text):
    #    response = self.chat.send_message(input_text)
    #    return response.text

    def get_response(self, symptoms):
        contents = types.Content(
            role='user',
            parts=[
                types.Part.from_text(text='Could you please recommend me what to do?'),
                types.Part.from_text(text=symptoms)
            ]
        )

        response = self.client.models.generate_content(
            model='gemini-2.0-flash',
            contents=contents,
            config=types.GenerateContentConfig(
                response_mime_type='application/json',
                response_schema=HealthcareAdvice
            )
        )
        #return response.text
        return response.to_json_dict()['parsed']#['likely_medical_conditions']

input_prompt = '''
You are acting as an experienced internist to whom patients come for diagnosis. Please perform the tasks listed below.
1. Analyze the symptoms given by the user.
2. Identify likely medical conditions.
3. Create a list of recommended home remedies to remedy the symptoms.
4. Recommend the type of specialist suited for the patient.
'''