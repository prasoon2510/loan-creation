import os
import requests
from dotenv import load_dotenv
load_dotenv()
base_url=os.getenv("BASE_URL")
offer_code=os.getenv("OFFER_CODE_ID")
user_id=os.getenv("USER_ID")
auth=os.getenv("AUTH_TOKEN")
headers={
    "UserId":user_id,
    "Type":"MERCHANT",
    "Content-Type":"application/json",
    "Authorization":auth
}

firstname=input("enter your first name:")
lastname=input("enter your last name:")
email=input("enter your email:")
mobile=input("enter your mobile.no:")

payload={
    "userInfo": [
        {
            "ipaddress": "10.190.3.74",
            "dateCreated": "2026-04-28 17:10:23"
        }
    ],
    "subProgram": "Windows",
    "loanAmount": 23900,
    "applicant": {
        "firstName": firstname,
        "lastName": lastname,
        "annualGrossIncome": 120000.00,
        "annualHouseHoldGrossIncome": 120000,
        "email": email,
        "address": {
            "country": "US",
            "zipCode": "78216",
            "city": "SAN ANTONIO",
            "street1": "11765 WEST AVENUE",
            "street2": None,
            "state": "TX"
        },
        "employmentStatus": "EMPLOYED",
        "occupation": "engineer",
        "currentEmployer": "finmkt",
        "mobile": mobile,
        "monthlyHousingPayment": 500.00,
        "citizenshipStatus": "USCITIZEN",
        "dateOfBirth": "1981-12-01",
        "identificationNumber": "666308630",
        "isbillingAddressSameAsInstallation": False,
        "installationAddress": {
            "country": "US",
            "zipCode": "78216",
            "city": "SAN ANTONIO",
            "street1": "11765 WEST AVENUE",
            "street2": "",
            "state": "TX"
        },
        "isPropertyOwned": True,
        "doYouResideAtTheProperty": True
    },
    "loanType": "POINT_OF_SALE"
}
url = f"{base_url}/gateway/v1/pos2/loan/publish"

response = requests.post(
    url,
    params={"offerCodeId": offer_code},
    headers=headers,
    json=payload,
    timeout=30,
)
if response.status_code == 200:
    print("Loan created, ID:", response.json()["loanId"])
else:
    print("Failed:", response.status_code, response.text)