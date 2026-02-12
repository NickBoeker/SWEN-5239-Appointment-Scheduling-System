from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
data_dict = {}
mid = 0

class Appointment(BaseModel):
    client: str
    provider: str
    appt_time: datetime


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/appointments/", response_description="Create a new appointment", status_code=status.HTTP_201_CREATED)
def create_appt(appt: Appointment):
    global data_dict
    global mid
    data_dict[mid] = appt
    mid += 1
    return {"appt_client": appt.client, "appt_datetime": appt.appt_time}

@app.get("/appointments/{appt_id}")
def read_appt(appt_id: int):
    global data_dict
    return {"appt_id": appt_id, "appt": data_dict[appt_id]}

@app.get("/appointments/")
def read_appts():
    global data_dict
    return {"appts": data_dict}