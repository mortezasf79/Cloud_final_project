import os
import time
import requests
import database_module
from dotenv import load_dotenv

load_dotenv()

def checking_function():
    while True:
        rows = database_module.getAllInfo()
        for row in rows:
            id = row['id']
            address = "http://" + row['address']
            # address = "http://www.google.com"
            # address = "http://216.239.38.120"
            print(address)
            try:
                response = requests.get(address)
                if response.status_code >= 200 and response.status_code < 300:
                        database_module.success_check(id=id)
                        print(f"The server at {'address'} is up and running.")
                else:
                        database_module.failure_check(id=id)
                        print(f"The server at {'address'} returned status code {response.status_code}.")
            except requests.exceptions.RequestException as e:
                database_module.failure_check(id=id)
                print(f"An error occurred while connecting to {address}: {e}")
            
        print(os.getenv('thread_time'))
        time.sleep(int(os.getenv('thread_time')))


def main():
    checking_function()

if __name__ == "__main__":
    main()