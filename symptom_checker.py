import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from healthcare_advice import HealthcareAdvice

input_prompt = '''
You are acting as an experienced internist to whom patients come for diagnosis. Please perform the tasks listed below.
1. Analyze the symptoms given by the user.
2. Identify likely medical conditions.
3. Create a list of recommended home remedies to remedy the symptoms.
4. Recommend the type of specialist suited for the patient.
Finally, please respond in the same language in which the user giver his/her symptoms.
'''

response_text = '''
- I understand you have these symptoms: {symptoms} \n
- Here is a list of the likely medical conditions: {likely_medical_conditions} \n
- Some of the things you can do to alleviate symptoms include: {recommendations} \n
- If symptoms persist, I recommend that you visit one of the following specialists: {specialists}
'''

load_dotenv()

class SymptomChecker:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
        #self.chat = self.client.chats.create(model='gemini-2.0-flash', history=[])

    def get_response(self, symptoms):
        contents = types.Content(
            role='user',
            parts=[
                types.Part.from_text(text=input_prompt),
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
        json_response = response.to_json_dict()['parsed']
        return response_text.format(
            symptoms = ', '.join(json_response['symptoms']),
            likely_medical_conditions = ', '.join(json_response['likely_medical_conditions']),
            recommendations=', '.join(json_response['recommendations']),
            specialists=', '.join(json_response['specialists'])
        )

