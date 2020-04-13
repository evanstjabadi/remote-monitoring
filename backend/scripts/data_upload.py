import requests

from time import sleep
from random import random
from datetime import datetime


BE_URL = "https://remote-monitoring.evanstjabadi.live/backend/randoms/"
LOCAL_URL = "http://127.0.0.1:5000/randoms/"


def data_log(data):
    with open('data_log.txt', 'a+') as file:
        file.write(data)
    return None


def data_upload():
    random_value = int(random() * 100)
    time_stamb = datetime.now()
    string_time_stamb = time_stamb.strftime("%Y-%m-%d %H:%M:%S")

    payload = {
        "value": random_value,
        "time_stamb": string_time_stamb
    }

    response = requests.post(BE_URL, json=payload)
    log = "Status Code: "+str(response.status_code)+'\n'+"Data: "+str(response.text)+'\n'
    data_log(log)


if __name__ == "__main__":
    while True:
        sleep(6)  # sleeps for 5 seconds
        data_upload()
