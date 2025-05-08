from pydantic import  BaseModel

class HealthcareAdvice(BaseModel):
    symptoms: list[str]
    likely_medical_conditions: list[str]
    recommendations: list[str]
    specialists: list[str]