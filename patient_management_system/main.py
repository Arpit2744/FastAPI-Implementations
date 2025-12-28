from fastapi import FastAPI, Path,HTTPException,Query
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
def view_patient(patient_id: str = Path(...,description = 'ID of the patient in the DB', examples='P001')):
    try:
        data = load_data() #load data
        for patient_record in data:
            if patient_record["patient_id"] == patient_id:
                logger.info("patient id reading")
                return patient_record
        raise HTTPException(status_code=404, detail="person not found")

    except HTTPException as e:
        raise e
    except Exception as e:
        raise CustomException(e,sys)

@app.get('/sort')
def sort_patient(sort_by: str=Query(...,description='sort on the basis of age'), order: str=Query('asc',description='sort in asc or desc order')):
    valid_fields = ['age']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"invalid field selected from {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f"invalid order selected between asc and desc")

    data = load_data()

    sort_order = True if order == 'desc' else False

    def get_sort_value(patient):
        if sort_by == 'age':
            return int(patient['personal_info']['age'])
        elif sort_by == 'name':
            return int(patient['personal_info']['name'])
        return 0
    sorted_data = sorted(data,key=get_sort_value,reverse=sort_order)

    return sorted_data
