import os
import requests

from dotenv import load_dotenv

load_dotenv()


def get_loan_details(loan_id):

    base_url = os.getenv("GET_API_BASE_URL")

    username = os.getenv("GET_API_USERNAME")
    password = os.getenv("GET_API_PASSWORD")

    user_id = os.getenv("USER_ID")
    location_id = os.getenv("LOCATION_ID")

    if not all([base_url, username, password, loan_id]):
        raise ValueError("Missing GET API configuration")

    url = f"{base_url}/{loan_id}"

    headers = {
        "UserId": user_id,
        "LocationId": location_id
    }

    print("\nFetching loan details...")
    print("GET URL:", url)

    response = requests.get(
        url,
        headers=headers,
        auth=(username, password),
        timeout=30
    )

    print("GET Status Code:", response.status_code)

    response.raise_for_status()

    loan_data = response.json()

    print("\nLoan Details:")
    print(loan_data)

    return loan_data
