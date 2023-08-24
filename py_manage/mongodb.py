import pymongo
from dotenv import load_dotenv
import os
from senzor import dht_sensor
from datetime import datetime

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

            current_date = datetime.now().strftime('%Y-%m-%d')

            doc = {
                "temperature": temperature,
                "humidity": humidity,
                "date": current_date,
            }

            rezultat = colection.insert_one(doc)

            print("ID-ul documentului inserat:", rezultat.inserted_id)

            client.close()

        except Exception:
            print("Error " + Exception)

    
    def insert_data(self, list_data):

        try:
            client = pymongo.MongoClient(self.url)

            db = client.mongodb
            colection = db[self.colection]

            print("urmeaza date")
            print(list_data)

            formatted_data = [
                {"temperature": item[0], "humidity": item[1], "date": item[2]}
                for item in list_data
            
            ]

            for item in list_data:
                print(item[1])
                print(item[2])

            # Inserarea datelor în colecție
            colection.insert_many(formatted_data)

            # rezultat = colection.insert_one(list_data)

            print("Datele s-au insertat cu succes")

            client.close()

        except Exception:
            print("Error " + str(Exception))

