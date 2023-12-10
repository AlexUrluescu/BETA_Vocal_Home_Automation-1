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

logging.info(f"URL_CONN: {URL_CONNECTION_DB}")
logging.info(f"COLLECTION_NAME: {COLLECTION_NAME}")


class GuiFlow():

    def __init__(self):
        self.mongoDatabase = MongoDatabase(URL_CONNECTION_DB, COLLECTION_NAME)
        self.localDatabase = LocalDatabase()
        self.internet_checker = internet_checker('data.db')
    
    def insertDataIntoDB(self, temperature, humidity) -> bool:
        exist_internet: bool = self.internet_checker.check_internet_connection()

        if(exist_internet):
            try:
                logging.info("intra in net")

                MongoDatabase.insert(temperature=temperature, humidity=humidity)
        
            except:
                pass
        
        else:
                logging.info("intra in fara net")
                success: bool = LocalDatabase.create()
                return success


    

guiFlow = GuiFlow()

result: str = guiFlow.insertDataIntoDB(temperature=23, humidity=99)

logging.info(f"result: {result}")