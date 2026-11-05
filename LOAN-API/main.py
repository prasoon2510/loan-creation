
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
    print("GET URL:", url)

    response = requests.get(
        url,
        headers=headers,
        auth=(username, password),
        timeout=30
    )

    print("\nGET Status Code:", response.status_code)

    if not response.ok:
        print("\nGET API Error Response:")
        print(response.text)

    response.raise_for_status()

    loan_data = response.json()

    print("\n========== COMPLETE LOAN DETAILS ==========")
    print(json.dumps(loan_data, indent=4))

    return loan_data


def main():

    try:

        print("================================")
        print("     LOAN DETAILS APPLICATION")
        print("================================")

        loan_details = get_loan_details()

        print("\n================================")
        print("GET API EXECUTION SUCCESSFUL")
        print("================================")

    except requests.exceptions.Timeout:
        print("\nError: GET API request timed out.")

    except requests.exceptions.ConnectionError:
        print("\nError: Unable to connect to GET API. Check network or DNS.")

    except requests.exceptions.HTTPError as error:
        print("\nHTTP Error:", error)

    except requests.exceptions.RequestException as error:
        print("\nRequest Error:", error)

    except ValueError as error:
        print("\nConfiguration or JSON Error:", error)

    except Exception as error:
        print("\nUnexpected Error:", error)


if __name__ == "__main__":
    main()
