from pydantic import  BaseModel

class HealthcareAdvice(BaseModel):
    symptoms: list[str]
    likely_medical_conditions: list[str]
    recommendations: list[str]
    type_of_specialist: list[str]