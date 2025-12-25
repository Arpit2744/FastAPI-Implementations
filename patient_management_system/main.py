from fastapi import FastAPI, Path
import json
import sys
from config import logger
from exception import CustomException
app = FastAPI()


def load_data():
    try:
        with open('patient_management_system/patients.json','r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        raise CustomException(e,sys)
        logger.info("data reading completed")

logger.info("Server started")
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
    try:
        data = load_data() #load data
        for patient_record in data:
            if patient_record["patient_id"] == patient_id:
                logger.info("patient id reading")
                return patient_record
        return {"patient not found"}
    except Exception as e:
        raise CustomException(e,sys)
