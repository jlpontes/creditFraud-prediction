# main.py

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# 1. Initialize the FastAPI app
# We provide a title and a version for our API
app = FastAPI(
    title="Fraud Detection API",
    version="1.0",
    description="An API to detect fraud in financial transactions using a Random Forest model."
)

# 2. Load our trained model
# This happens only once when the API starts up.
model = joblib.load('fraud_model.joblib')

# 3. Define the input data format with Pydantic
# This ensures that any data sent to the API will have the correct format and data types.
class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    scaled_amount: float
    scaled_time: float

# 4. Create the prediction endpoint
# @app.post("/predict") tells FastAPI to create an endpoint that accepts POST requests
@app.post("/predict")
def predict_fraud(transaction: Transaction):
    """
    Receives transaction data, makes a prediction using the trained model, and returns the classification.
    - **transaction**: A JSON object with the transaction data.
    """
    # Convert the received data into a Pandas DataFrame, as the model was trained with it.
    input_data = pd.DataFrame([transaction.dict()])
    
    # Make the prediction
    prediction = model.predict(input_data)[0]
    
    # Get the prediction probability
    prediction_proba = model.predict_proba(input_data)[0]
    
    # Define the result
    is_fraud = bool(prediction) # Converts the result (0 or 1) to boolean (False or True)
    
    # Return the result in JSON format
    return {
        "is_fraud": is_fraud,
        "fraud_probability": f"{prediction_proba[1]*100:.2f}%"
    }

# This block allows running the API directly with "python main.py", although uvicorn is recommended
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
