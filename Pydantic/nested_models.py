from pydantic import BaseModel


class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'meerut', 'state': 'UP', 'pin': '241301'}

address1 = Address(**address_dict)

patient_dict = {
    'name': 'arpit',
    'gender': 'male',
    'age': 35,
    'address': address1
}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

# better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., patient,MedicalRecord)

# Readability: Easier for developer and API consumer to understand

# Validation: Nested models are validated automatically-no extra work needed