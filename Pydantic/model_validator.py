from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model

"""
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. 
Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. 
Deprecated in Pydantic V2.12 to be removed in V3.0.
  @model_validator(mode='after')
"""

def update_patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(f"Verified Email: {patient.email}")
    print("Database Updated Successfully")
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print("updated the database")

patient_info = {
    'name': 'arpit',
    'age':80,
    'email':'asingh@hdfc.com',
    'linkedin_url':'https://www.hdfc.com',
    'weight':60.5,
    'married':True,
    'allergies':['pollen','dust'],
    'contact_details':{'phone_no':'+918382837473','email':'asjj383@gmail.com','emergency':'82717287'}
    }

# IMPORTANT LINE:
# We are converting the dictionary 'patient_info' into a 'Patient' Object.
# The ** (double star) unpacks the dictionary.
# It's like saying: Patient(name='arpit', age=20, weight=60.5...)
patient1 = Patient(**patient_info) # validation -> type coercion 

update_patient_info(patient1)
