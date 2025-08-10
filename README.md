# Sistema de Detecção de Fraudes em Transações com API

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green?style=for-the-badge&logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.1.2-orange?style=for-the-badge&logo=scikit-learn)
![Docker](https://img.shields.io/badge/Docker-20.10-blue?style=for-the-badge&logo=docker)

## 📖 Descrição do Projeto

Este projeto implementa um sistema de Machine Learning end-to-end para a detecção de fraudes em transações financeiras em tempo real. O objetivo foi desenvolver uma solução completa, desde a análise exploratória dos dados e treinamento de um modelo de alta performance, até a sua implantação como uma API robusta pronta para produção.

O modelo foi treinado no dataset "Credit Card Fraud Detection" disponível no Kaggle e alcançou um **recall de 92%** no conjunto de teste, demonstrando alta eficácia na identificação de transações fraudulentas.

## ✨ Funcionalidades

- **Análise de Dados Completa:** Notebooks detalhados com a análise exploratória e insights.
- **Modelo de Machine Learning:** Utiliza um `RandomForestClassifier` treinado e otimizado para alta performance em dados desbalanceados.
- **API em Tempo Real:** Uma API construída com **FastAPI** que expõe o modelo, permitindo que outros sistemas façam previsões em tempo real.
- **Validação de Dados:** Utiliza Pydantic para garantir que os dados enviados à API estejam no formato correto.
- **Pronto para Produção:** A aplicação é containerizada com **Docker**, garantindo a portabilidade e a facilidade de implantação em qualquer ambiente.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.9+
- **Análise de Dados:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **API:** FastAPI
- **Servidor:** Uvicorn
- **Containerização:** Docker

## 🚀 Como Executar o Projeto

Siga os passos abaixo para ter a aplicação rodando localmente.

### Pré-requisitos

- Python 3.9 ou superior
- Pip (ou Pip3)
- Docker (para o Módulo 5)

### 1. Clonar o Repositório

```bash
git clone [https://github.com/](https://github.com/)[SEU-NOME-DE-USUARIO]/[NOME-DO-SEU-REPOSITORIO].git
cd [NOME-DO-SEU-REPOSITORIO]
```

### 2. Criar e Instalar as Dependências

É uma boa prática criar um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale todas as bibliotecas necessárias:

```bash
pip3 install -r requirements.txt
```
*(**Nota:** Se você ainda não tem um arquivo `requirements.txt`, gere um com o comando: `pip3 freeze > requirements.txt`)*

### 3. Executar a API

Com as dependências instaladas, inicie o servidor FastAPI:

```bash
python3 -m uvicorn main:app --reload
```

O servidor estará rodando e acessível no seu navegador.

### 4. Acessar a Documentação e Testar

Abra seu navegador e vá para o seguinte endereço para acessar a documentação interativa e testar os endpoints:

**`http://127.0.0.1:8000/docs`**

## 🏗️ Estrutura do Projeto (Sugestão)

```
.
├── notebooks/
│   └── 1_analise_e_modelagem.ipynb
├── .gitignore
├── fraud_model.joblib
├── main.py
├── requirements.txt
└── README.md
```

## 📈 Próximos Passos

- Implementar um pipeline de CI/CD (GitHub Actions) para automatizar testes e deploy.
- Implantar a aplicação em um serviço de nuvem (ex: AWS, Google Cloud Run).
- Adicionar um sistema de logging e monitoramento para a API e para o modelo.
