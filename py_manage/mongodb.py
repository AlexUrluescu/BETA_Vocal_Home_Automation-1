import pymongo
from dotenv import load_dotenv
import os
from senzor import dht_sensor

senzor = dht_sensor()

class connMongo():
    def __init__(self, url, colection):
        self.url = url
        self.colection = colection


    def insert_data_cloud(self, temperature, humidity):
        try:
            client = pymongo.MongoClient(self.url)

            db = client.mongodb
            colection = db[self.colection]

            documents = colection.find()

            for document in documents:
                data = document

            print(temperature)
            print(humidity)

            doc = {
                "temperature": temperature,
                "humidity": humidity,
                "date": "2023-06-25",
            }

            rezultat = colection.insert_one(doc)

            print("ID-ul documentului inserat:", rezultat.inserted_id)

            client.close()

        except Exception:
            print("Error " + Exception)

