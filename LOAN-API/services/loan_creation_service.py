
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


def get_loan_details():

    url = os.getenv("GET_API_URL")
    username = os.getenv("GET_API_USERNAME")
    password = os.getenv("GET_API_PASSWORD")
    user_id = os.getenv("USER_ID")

    if not all([url, username, password]):
        raise ValueError("Missing GET API configuration in .env")

    headers = {
        "Accept": "application/json"
    }

    if user_id:
        headers["UserId"] = user_id

    print("\nFetching loan details using GET API...")

    response = requests.get(
        url,
        headers=headers,
        auth=(username, password),
        timeout=30
    )

    print("GET Status Code:", response.status_code)

    if not response.ok:
        print("GET API Error:", response.text)

    response.raise_for_status()

    response_data = response.json()

    print("\nGET API JSON Response:")
    print(json.dumps(response_data, indent=4))

    return response_data
