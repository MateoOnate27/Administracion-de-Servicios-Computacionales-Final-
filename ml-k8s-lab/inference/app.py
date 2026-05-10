from fastapi import FastAPI
import pickle
import numpy as np
import os

app = FastAPI()

MODEL_PATH = "/mnt/model/model.pkl"

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(data: dict):
    # Usamos dict para que sea más flexible con las librerías
    if not os.path.exists(MODEL_PATH):
        return {"error": "Modelo no encontrado"}
    
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    
    # Extraemos la lista de la llave 'input'
    input_data = np.array(data['input'])
    prediction = model.predict(input_data)
    return {"prediction": prediction.tolist()}
