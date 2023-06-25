import requests

# Funcția pentru a trimite datele către API în cloud
def send_sensor_data_to_cloud(data):
    # url = 'https://smarthome-dowt.onrender.com/datasenzor' 
    url = 'http://localhost:5000/datasenzor' # Inlocuiți cu URL-ul real al API-ului în cloud

    # Trimiteți datele prin cererea POST către API-ul în cloud
    response = requests.post(url, json=data)

    # Verificați răspunsul de la API
    if response.status_code == 200:
        print('Datele au fost trimise cu succes către API în cloud.')

        data = response.json()
        print(data)
    else:
        print('Eroare la trimiterea datelor către API în cloud.')

# Exemplu de date de la senzori
sensor_data = {
    'temperature': 23.5,
    'humidity': 59.2,
    # alte date de la senzori
}

# Apelați funcția pentru a trimite datele către API în cloud
send_sensor_data_to_cloud(sensor_data)
