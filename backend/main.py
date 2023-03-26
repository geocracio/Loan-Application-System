import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
from fastapi.middleware.cors import CORSMiddleware


class RequestBody(BaseModel):
    Income: int | None = None
    Age: int | None = None
    Experience: int | None = None
    CURRENT_JOB_YRS: int | None = None
    CURRENT_HOUSE_YRS: int | None = None
    MaritalStatus: str | None = None
    House_Ownership: str | None = None
    Car_Ownership: str | None = None
    Profession: str | None = None


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
    data = data.dict()
    df = pd.DataFrame(data, index=[0])
    pred, prob = make_prediction(df)
    return {'prediction': int(pred), 'probability': float(prob)}


data = {
  "Income": 1303834,
  "Age": 23,
  "Experience": 3,
  "CURRENT_JOB_YRS": 3,
  "CURRENT_HOUSE_YRS": 13,
  "MaritalStatus": "single",
  "House_Ownership": "rented",
  "Car_Ownership": "no",
  "Profession": "Mechanical_engineer",
}
df = pd.DataFrame(data, index=[0])
pred, prob = make_prediction(df)
