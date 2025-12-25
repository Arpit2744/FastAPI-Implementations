from fastapi import FastAPI, Path
import json


app = FastAPI()

def load_data():
    with open('notes/patients.json','r') as f:
        data = json.load(f)
        return data

@app.get('/')
def hello():
    return {'message': 'Patients Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patients record'}

@app.get('/view')
def view():
    data = load_data()

    return data

#check patient info through id
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(...,description = 'ID of the patient in the DB', example='P001')):
    data = load_data() #load data

    if patient_id in data:
        return data[patient_id]
    return {"patient not found"}

