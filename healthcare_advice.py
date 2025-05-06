from pydantic import  BaseModel

class HealthcareAdvice(BaseModel):
    likely_medical_conditions: str
    type_of_specialist: str