
import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()


def create_loan():

    url = os.getenv("POST_API_URL")
    offer_code_id = os.getenv("OFFER_CODE_ID")

    username = os.getenv("POST_API_USERNAME")
    password = os.getenv("POST_API_PASSWORD")

    user_id = os.getenv("USER_ID")

    if not all([url, offer_code_id, username, password, user_id]):
        raise ValueError("Missing POST API configuration in .env")

    with open("loan_payload.json", "r") as file:
        payload = json.load(file)

    headers = {
        "UserId": user_id,
        "Type": "MERCHANT",
        "Content-Type": "application/json"
    }

    params = {
        "offerCodeId": offer_code_id
    }

    print("Creating loan...")

    response = requests.post(
        url,
        params=params,
        json=payload,
        headers=headers,
        auth=(username, password),
        timeout=30
    )

    print("POST Status Code:", response.status_code)
    print("POST Response:", response.text)

    response.raise_for_status()

    response_data = response.json()

    loan_id = response_data.get("loanId")

    if not loan_id:
        raise ValueError(
            "loanId not found in POST API response"
        )

    print("Loan created successfully")
    print("Loan ID:", loan_id)

    return loan_id
