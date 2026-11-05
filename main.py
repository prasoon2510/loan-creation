
import os
<<<<<<< HEAD
from dotenv import load_dotenv
from services.loan_service import create_loan


def main():

    load_dotenv()

    dry_run = os.getenv("DRY_RUN", "true").lower() == "true"

    if dry_run:
        print("DRY RUN MODE")
        print("Configuration loaded successfully.")
        print("No loan creation request was sent.")
        print("Set DRY_RUN=false after authorization to submit.")
        return

    try:
        response = create_loan()

        print("Loan created successfully!")
        print("Loan ID:", response.get("loanId"))
        print("Loan URL:", response.get("loan_url"))

    except Exception as error:
        print("Loan creation failed:", error)


if __name__ == "__main__":
    main()
=======

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
>>>>>>> 73b34e194167ec813cde7be708380a48874d4c58
