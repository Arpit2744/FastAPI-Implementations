from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool          
    allergies: List[str]   
    contact_details: Dict[str, str] 

    @computed_field
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

def update_patient_data(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"BMI: {patient.bmi}") 
    print('updated')

patient_info = {
    'name': 'arpit',
    'email': 'asingh92@gmail.com',
    'age': '34',
    'weight': 66.4,
    'height': 1.74,
    'married': True,
    'allergies': ['dust'],
    'contact_details': {'phone': '1234'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)