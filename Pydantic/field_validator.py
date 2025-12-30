from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value: str) -> str:

        valid_domains = ['hdfc.com','icici.com']

        domain_name = value.split('@')[1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 to 100')

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
    'age':20,
    'email':'asingh@hdfc.com',
    'linkedin_url':'https://www.hdfc.com',
    'weight':60.5,
    'married':True,
    'allergies':['pollen','dust'],
    'contact_details':{'phone_no':'+918382837473','email':'asjj383@gmail.com'}
    }

# IMPORTANT LINE:
# We are converting the dictionary 'patient_info' into a 'Patient' Object.
# The ** (double star) unpacks the dictionary.
# It's like saying: Patient(name='arpit', age=20, weight=60.5...)
patient1 = Patient(**patient_info) # validation -> type coercion 

update_patient_info(patient1)