import sqlite3
import pymongo
from dotenv import load_dotenv
import os
from senzor import dht_sensor
from datetime import datetime
import logging

senzor = dht_sensor()
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class MongoDatabase():
    def __init__(self, url, colection):
        self.url = url
        self.colection = colection

        self.connection: sqlite3.Connection = sqlite3.connect('data.db')
        self.cursor: sqlite3.Cursor = self.connection.cursor()


    def insert(self, temperature, humidity):
        try:
            client = pymongo.MongoClient(self.url)

            db = client.mongodb
            colection = db[self.colection]

            documents = colection.find()

            for document in documents:
                data = document

            logging.info(temperature)
            logging.info(humidity)

            current_date = datetime.now().strftime('%Y-%m-%d')

            doc = {
                "temperature": temperature,
                "humidity": humidity,
                "date": current_date,
            }

            rezultat = colection.insert_one(doc)

            logging.info("ID-ul documentului inserat:", rezultat.inserted_id)

            client.close()

        except Exception:
            logging.info("Error " + Exception)

    
    def insert_data(self, list_data):

        try:
            client = pymongo.MongoClient(self.url)

            db = client.mongodb
            colection = db[self.colection]

            logging.info("urmeaza date")
            logging.info(list_data)

            formatted_data = [
                {"temperature": item[0], "humidity": item[1], "date": item[2]}
                for item in list_data
            
            ]

            for item in list_data:
                logging.info(item[1])
                logging.info(item[2])

            # Inserarea datelor în colecție
            colection.insert_many(formatted_data)

            # rezultat = colection.insert_one(list_data)

            logging.info("Datele s-au insertat cu succes")

            client.close()

        except Exception:
            logging.info("Error " + str(Exception))

