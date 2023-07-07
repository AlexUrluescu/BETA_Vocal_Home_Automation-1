import urllib.request
import time
import sqlite3
from dotenv import load_dotenv
import os
from senzor import dht_sensor
from mongodb import connMongo

class internet_checker():
    def __init__(self, timer):
        self.timer = timer

    def check_internet_connection(self):
        url = "http://www.google.com"
        timeout = 5
        try:
            urllib.request.urlopen(url, timeout=timeout)
            return True
        except urllib.request.URLError:
            return False


    def create_local_database(self):
        conn = sqlite3.connect("local_database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, temperature NUMBER, humidity NUMBER, date DATETIME)")
        conn.commit()
        conn.close()


    def insert_data_local(self, temperature, humidity, date):
        try:
            conn = sqlite3.connect("local_database.db")
            c = conn.cursor()

            c.execute(f"INSERT INTO data (temperature, humidity, date) VALUES ({temperature}, {humidity}, {date})")

            conn.commit()
            conn.close()
        
        except sqlite3.Error as err:
            print("Eroare de inserare:", err)

senzor = dht_sensor()
temperature = senzor.get_t()
humidity = senzor.get_h()
        
load_dotenv()
URL_CONN = os.getenv("URL_CONNECTION")
COLECTION = os.getenv("COLECTION")

checker = internet_checker(5)

mongo =  connMongo(URL_CONN, COLECTION)


while True:
    if checker.check_internet_connection():
        print("Conexiunea la internet este activă.")
        print(f"temperature: {temperature}")
        print(f"humidity: {humidity}")

        mongo.insert_data_cloud(temperature=temperature, humidity=humidity)

        temperature = senzor.get_t()
        humidity = senzor.get_h()

    else:
        print("Nu există conexiune la internet.")
        checker.create_local_database()
        checker.insert_data_local(temperature, humidity, "12-07-2023")
            
    time.sleep(checker.timer)  # Verifică conexiunea la internet la fiecare 5 secunde