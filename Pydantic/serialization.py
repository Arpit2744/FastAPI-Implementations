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

temp = patient1.model_dump() #exlude,include can be used in this function exclude_unset aswell

print(temp)
