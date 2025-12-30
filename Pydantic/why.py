from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name: Annotated[str,Field(max_length=50, title='name of the patient', description='Give the name of the patient in less than 50 characters',examples=['arpit','amit'])]
    age: int = Field(gt=0,lt=120)
    email: EmailStr
    linkedin_url: AnyUrl
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description='is the patient married or not')]
    allergies: Annotated[Optional[list[str]], Field(default=None,max_length=5)]
    contact_details: Dict[str,str]

def insert_patient_info(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print('inserted into database')

def update_patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print("updated the database")

patient_info = {
    'name': 'arpit',
    'age':20,
    'email':'asingh@gmail.com',
    'linkedin_url':'https://www.linked.com',
    'weight':60.5,
    'married':True,
    'allergies':['pollen','dust'],
    'contact_details':{'phone_no':'+918382837473','email':'asjj383@gmail.com'}
    }
# IMPORTANT LINE:
# We are converting the dictionary 'patient_info' into a 'Patient' Object.
# The ** (double star) unpacks the dictionary.
# It's like saying: Patient(name='arpit', age=20, weight=60.5...)
patient1 = Patient(**patient_info)

update_patient_info(patient1)
"""
1. define a pydantic model that represents the ideal schema of the data
this includes the expected fields their types and any validation constraints(e.g. gt=0 for any +ive number)

2. instantiate the model with raw inout data (usually a dictionary or json like structure)
pydantic will automatically validate the data and coerce it into the correct python types (if possibl)
if the data doesn't meet the model requirements pydantic raises a validation error

3. pass the validated model object to function or use it throughout your codebase
this ensures that every part of your program works with clean type-safe and logically valid data
"""
