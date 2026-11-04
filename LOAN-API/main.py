
import os

from dotenv import load_dotenv

from services.loan_creation_service import create_loan
from services.loan_details_service import get_loan_details


load_dotenv()


def main():

    try:

        if os.getenv("DRY_RUN", "true").lower() == "true":
            print("DRY_RUN is enabled.")
            print("No loan will be created.")
            print("Set DRY_RUN=false to execute the POST and GET workflow.")
            return

        loan_id = create_loan()

        print("\n--------------------------------")
        print("POST API COMPLETED")
        print("--------------------------------")

        loan_details = get_loan_details(loan_id)

        print("\n--------------------------------")
        print("COMPLETE LOAN DETAILS")
        print("--------------------------------")

        print(loan_details)

    except Exception as error:

        print("\nAPI operation failed:")
        print(error)


if __name__ == "__main__":
    main()
