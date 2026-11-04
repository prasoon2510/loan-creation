
import os

from fastapi import FastAPI

app = FastAPI(title="Loan Management API")

APP_ENV = os.getenv("APP_ENV", "development")


@app.get("/")
def home():
    return {
        "message": "Welcome to Loan Management API",
        "environment": APP_ENV
    }


@app.get("/loan/{loan_id}")
def get_loan(loan_id: int):

    return {
        "loan_id": loan_id,
        "customer_name": "Sravan",
        "loan_amount": 500000,
        "status": "APPROVED",
        "environment": APP_ENV
    }


@app.get("/health")
def health_check():
    return {
        "status": "Application is running"
    }
