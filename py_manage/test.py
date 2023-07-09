import requests
from senzor import dht_sensor  
from time import sleep

def send_sensor_data_to_cloud(senzor_data):
    url = 'https://smarthome-dowt.onrender.com/datasenzor' 
    # url = 'http://localhost:5000/datasenzor' 

    response = requests.post(url, json=senzor_data)

    if response.status_code == 200:
        print('Datele au fost trimise cu succes către API în cloud.')

        data = response.json()
        print(data)
    else:
        print('Eroare la trimiterea datelor către API în cloud.')


senzor = dht_sensor()

while True:
    temp = senzor.get_t()
    hum = senzor.get_h()

    sensor_data = {
        'temperature': temp,
        'humidity': hum,
    }

    send_sensor_data_to_cloud(sensor_data)

    sleep(5)
