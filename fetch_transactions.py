import requests
import time
from datetime import datetime

def fetch_success_transactions():
    url = "https://atksmv-traders.onrender.com/admin/dashboard"
    while True:
        current_time = datetime.now().time()
        print(current_time.hour)
        if not (0 <= current_time.hour < 6):
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
                transactions = response.json()
                if transactions is not None:
                    print("Success Transactions:")
                    print(transactions)
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"An error occurred: {err}")
        time.sleep(14*60)  # Sleep for 14 minutes

if __name__ == "__main__":
    fetch_success_transactions()

