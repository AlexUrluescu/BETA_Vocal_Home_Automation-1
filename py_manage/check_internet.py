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

    def create_local_dbStatus(self):
        conn = sqlite3.connect("local_database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS status_db (id INTEGER PRIMARY KEY, status NUMBER)")
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


    def insert_status_local(self, status):
        try:
            conn = sqlite3.connect("local_database.db")
            c = conn.cursor()

            c.execute(f"INSERT INTO status_db (status) VALUES ({status})")

            conn.commit()
            conn.close()
        except sqlite3.Error as err:
            print("Eroare de inserare:", err)

    
    def get_local_data(self, data_list):
        try:
            conn = sqlite3.connect("local_database.db")
            c = conn.cursor()

            c.execute("SELECT * FROM data")

            data = c.fetchall()
            print(data)

            data_list = data

            conn.commit()
            conn.close()

            return data
        
        except sqlite3.Error as err:
            print("Eroare de inserare:", err)


    def delete_local_data(self, name_table):
        try:
            conn = sqlite3.connect("local_database.db")
            c = conn.cursor()

            c.execute(f"DELETE FROM {name_table}")

            print("datele s-au sters")

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

        data_list = []

        data_list2 = checker.get_local_data(data_list)
        print(data_list2)

        # data_list2 = []
        if len(data_list2) == 0:
            print("Nu exista date stocate in local")
            mongo.insert_data_cloud(temperature=temperature, humidity=humidity)

        else:
            print("Exista date stocate local")
            print(data_list2)
            # doc = {
            #     "temperature": temperature,
            #     "humidity": humidity,
            #     "date": "2023-06-25",
            # }
            mongo.insert_data(data_list2)
            checker.delete_local_data('data')

        temperature = senzor.get_t()
        humidity = senzor.get_h()

    else:
        print("Nu există conexiune la internet.")
        checker.create_local_database()
        checker.insert_data_local(temperature, humidity, "12-07-2023")
        # checker.create_local_dbStatus()
        # checker.insert_status_local()
        print(f"temp: {temperature}")
        print(f"hum: {humidity}")

        temperature = senzor.get_t()
        humidity = senzor.get_h()
            
    time.sleep(checker.timer)  # Verifică conexiunea la internet la fiecare 5 secunde