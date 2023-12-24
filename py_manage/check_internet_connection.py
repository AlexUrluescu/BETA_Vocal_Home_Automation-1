import urllib.request
import time
import sqlite3
from dotenv import load_dotenv
import os
from senzor import dht_sensor
from mongodb import MongoDatabase
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class internet_checker():

    def check_internet_connection(self) -> bool:
        url: str = "http://www.google.com"
        timeout: int = 5
        try:
            urllib.request.urlopen(url, timeout=timeout)
            return True
        except urllib.request.URLError:
            return False



# senzor = dht_sensor()
# temperature = senzor.get_t()
# humidity = senzor.get_h()
# # current_date = str(current_date)
        
# load_dotenv()
# URL_CONN = os.getenv("URL_CONNECTION")
# COLECTION = os.getenv("COLECTION")

# checker = internet_checker(5)

# mongo =  Database(URL_CONN, COLECTION)


# while True:
#     if checker.check_internet_connection():
#         print("Conexiunea la internet este activă.")
#         print(f"temperature: {temperature}")
#         print(f"humidity: {humidity}")

#         # checker.create_local_database()

#         data_list = []

#         data_list2 = checker.get_local_data(data_list)
#         print(data_list2)

#         # data_list2 = []
#         if len(data_list2) == 0:
#             print("Nu exista date stocate in local")
#             mongo.insert_data_cloud(temperature=temperature, humidity=humidity)

#         else:
#             print("Exista date stocate local")
#             print(data_list2)
#             # doc = {
#             #     "temperature": temperature,
#             #     "humidity": humidity,
#             #     "date": "2023-06-25",
#             # }
#             mongo.insert_data(data_list2)
#             checker.delete_local_data('data')

#         temperature = senzor.get_t()
#         # current_date = datetime.datetime.now()
#         humidity = senzor.get_h()

#     else:
#         print("Nu există conexiune la internet.")
#         checker.create_local_database()
#         checker.insert_data_local(temperature, humidity)
#         # checker.create_local_dbStatus()
#         # checker.insert_status_local()
#         print(f"temp: {temperature}")
#         print(f"hum: {humidity}")


#         temperature = senzor.get_t()
#         humidity = senzor.get_h()
#         # current_date = datetime.datetime.now()
            
#     time.sleep(checker.timer)  # Verifică conexiunea la internet la fiecare 5 secunde