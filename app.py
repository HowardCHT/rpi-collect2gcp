from dotenv import load_dotenv
import os
import requests
from time import sleep

load_dotenv()

if __name__ == "__main__":
    url_getdata = os.getenv('URL_GETDATA')
    url_cloudfunction = os.getenv('URL_CLOUDFUNCTION')
    upload_interval = int(os.getenv('UPLOAD_INTERVAL', default=30))

    print(f"url_getdata = {url_getdata}")
    print(f"url_cloudfunction = {url_cloudfunction}")
    print(f"upload_interval = {upload_interval}")

    while True:
        try:
            print("-------- Get RPi sensor data --------")
            RPi_requests = requests.get(url_getdata)
            print(f"Return code => {RPi_requests.status_code}")
            if RPi_requests.ok:
                CJMCU_data = RPi_requests.json()
                print(CJMCU_data)
                r = requests.post(url_cloudfunction, json=CJMCU_data)
                print(f"Post to cloud function return code => {r.status_code}")
            else:
                print(RPi_requests.text)
            
            sleep(upload_interval)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"error => {e}")
