import pandas as pd
from fastapi import FastAPI, Request
from pydantic import BaseModel
from joblib import load
from fastapi.middleware.cors import CORSMiddleware


class RequestBody(BaseModel):
    income: int | None = None
    age: int | None = None
    experience: int | None = None
    maritalStatus: str | None = None
    houseOwnership: str | None = None
    carOwnership: str | None = None
    profession: str | None = None
    currentJobYears: int | None = None
    currentHouseYear: int | None = None


def make_prediction(data: pd.DataFrame):
    clf = load('assets/pipeline.joblib')
    prediction = clf.predict(data)[0]
    probability = clf.predict_proba(data)[:, 1][0]
    return prediction, probability


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/predict')
async def predict(data: RequestBody):
    model_input = {
        "Income": data.income,
        "Age": data.age,
        "Experience": data.experience,
        "CURRENT_JOB_YRS": data.currentJobYears,
        "CURRENT_HOUSE_YRS": data.currentHouseYear, 
        "MaritalStatus": data.maritalStatus,
        "House_Ownership": data.houseOwnership,
        "Car_Ownership": data.carOwnership,
        "Profession": data.profession,
    }
    df = pd.DataFrame([model_input])
    pred, prob = make_prediction(df)
    print(pred, prob)
    return {'prediction': int(pred), 'probability': float(prob)}

# data = {
#   "Income": 1303834,
#   "Age": 23,
#   "Experience": 3,
#   "CURRENT_JOB_YRS": 3,
#   "CURRENT_HOUSE_YRS": 13,
#   "MaritalStatus": "single",
#   "House_Ownership": "rented",
#   "Car_Ownership": "no",
#   "Profession": "Mechanical_engineer",
# }
# df = pd.DataFrame(data, index=[0])
# pred, prob = make_prediction(df)
