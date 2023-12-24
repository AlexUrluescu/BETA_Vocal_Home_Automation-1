from mongodb import MongoDatabase
from localdb import LocalDatabase
from check_internet_connection import internet_checker
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
load_dotenv()
URL_CONNECTION_DB = os.getenv("URL_CONNECTION_DB")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

class GuiFlow():

    def __init__(self):
        self.mongoDatabase = MongoDatabase(URL_CONNECTION_DB, COLLECTION_NAME)
        self.localDatabase = LocalDatabase()
        self.internet_checker = internet_checker()
    
    def insertDataIntoDB(self, temperature, humidity) -> bool:
        exist_internet: bool = self.internet_checker.check_internet_connection()

        if(exist_internet):
            try:
                logging.info("intra in net")

                data: list[str] =  self.localDatabase.getData();
                logging.info(f"data from local: {data}")

                if(len(data) != 0):
                     logging.info(f"Exist local data: {data}")

                     self.mongoDatabase.insert_data(data)
                     self.localDatabase.delete()
                
                else:
                     logging.info(f"dont exist local data")

                self.mongoDatabase.insert(temperature=temperature, humidity=humidity)
                logging.info(f'insert into mongo temp: {temperature} and hum: {humidity}')
        

            except Exception:
                logging.info(Exception)
        
        else:
                logging.info("intra in fara net")
                success: bool = self.localDatabase.create()

                if(success):
                    self.localDatabase.insert(temperature=temperature, humidity=humidity)

                data =  self.localDatabase.getData();
                logging.info(f"data from local: {data}")

