import requests


from time import sleep
from random import random
from datetime import datetime


BE_URL = "https://remote-monitoring.evanstjabadi.live/backend/randoms/"
LOCAL_URL = "http://127.0.0.1:5000/randoms/""


def data_upload():
    random_value = int(random() * 100)
    time_stamb = datetime.now()
    print(time_stamb)

    payload = {
        "value": random_value,
        "time_stamb": str(time_stamb)
    }

    response = requests.post(LOCAL_URL, json=payload)
    print(response.status_code)


if __name__ == '__main__':
    while True:
        sleep(5)  # sleeps for 5 seconds
        data_upload()
