from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from api.schemas import ShipmentInput

app = FastAPI(
    title="E-Commerce Shipment Delivery Prediction API",
    description="Predict whether an e-commerce shipment will reach on time or be delayed."
)
MODEL_PATH = Path(__file__).resolve().parents[1] / 'models' / 'ecommerce_shipment_final_model.joblib'
model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None

@app.get('/')
def home():
    return {'message':'E-Commerce Shipment Prediction API is running'}

@app.get('/health')
def health():
    return {'status':'ok','model_loaded': model is not None}

@app.post('/predict')
def predict(payload: ShipmentInput):
    if model is None:
        raise HTTPException(status_code=500, detail='Model file not found. Run the notebook and place the model in models/.')
    X = pd.DataFrame([payload.model_dump()])
    pred = int(model.predict(X)[0])
    result = 'Reached on time' if pred == 1 else 'Not reached on time'
    response = {'prediction': pred, 'result': result}
    if hasattr(model, 'predict_proba'):
        response['probability'] = float(model.predict_proba(X)[0][pred])
    return response
