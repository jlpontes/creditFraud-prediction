# main.py3
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# 1. Inicializar o objeto da API
#título e uma versão para a nossa API
app = FastAPI(
    title="API de Detecção de Fraude",
    version="1.0",
    description="Uma API para detectar fraudes em transações financeiras usando um modelo de Random Forest."
)

# 2. Carregar nosso modelo treinado

model = joblib.load('fraud_model.joblib')

# 3. Definir o formato dos dados de entrada com Pydantic
# Isso garante que qualquer dado enviado para a API terá o formato correto.
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

# 4. Criar o endpoint de previsão
# @app.post("/predict") diz ao FastAPI para criar um endpoint que aceita requisições do tipo POST
@app.post("/predict")
def predict_fraud(transaction: Transaction):
    """
    Recebe os dados de uma transação, faz a previsão usando o modelo treinado e retorna a classificação.
    - **transaction**: Um objeto JSON com os dados da transação.
    """
    # Converter os dados recebidos para um DataFrame do Pandas, pois o modelo foi treinado com ele.
    input_data = pd.DataFrame([transaction.dict()])
    
    # Fazer a previsão
    prediction = model.predict(input_data)[0]
    
    # Obter a probabilidade da previsão
    prediction_proba = model.predict_proba(input_data)[0]
    
    # Definir o resultado
    is_fraud = bool(prediction) # Converte o resultado (0 ou 1) para booleano (False ou True)
    
    # Retornar o resultado em formato JSON
    return {
        "is_fraud": is_fraud,
        "fraud_probability": f"{prediction_proba[1]*100:.2f}%"
    }

# Este bloco permite rodar a API diretamente com "python main.py", embora uvicorn seja o recomendado
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
