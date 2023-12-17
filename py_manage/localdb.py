import sqlite3
import pymongo
from dotenv import load_dotenv
import os
from senzor import dht_sensor
from datetime import datetime
import logging

senzor = dht_sensor()
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class LocalDatabase():
    def __init__(self):
        self.databaseName = 'data.db'
        self.connection: sqlite3.Connection = sqlite3.connect(self.databaseName)
        self.cursor: sqlite3.Cursor = self.connection.cursor()

    
    def getData(self) -> list[str]:

        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM data;')
        data = cursor.fetchall()
        cursor.close()
        connection.close()

        return data

    
    def create(self):
        # Creează tabela 'weather' cu cele trei coloane: temperatura, umiditate și data
        try:    
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS data (
                                temperature REAL,
                                humidity REAL,
                                data TEXT
                            )''')

            connection.commit() # Salvează modificările
            connection.close()  # Închide conexiunea
            return True
        except sqlite3.Error as error:
            logging.info(f"Error into the create_local_databse method: {error}")


    def createStatus(self):
        # conn = sqlite3.connect("data.db")
        # cursor = conn.cursor()
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS status_db (id INTEGER PRIMARY KEY, status NUMBER)")
            self.connection.commit()
            self.connection.close()
        except sqlite3.Error as error:
            logging.info(f"Error into the create_local_dbStatus method: {error}")


    def insert(self, temperature: str, humidity: str) -> bool:
        try:
            # conn = sqlite3.connect('data.db')
            # cursor = conn.cursor()

            # Obține data curentă și convert-o la formatul dorit (YYYY-MM-DD)
            data_curenta: str = datetime.now().strftime('%Y-%m-%d')


            # Inserează datele în tabela 'weather'
            self.cursor.execute('INSERT INTO data (temperature, humidity, data) VALUES (?, ?, ?)',
                        (temperature, humidity, data_curenta))

            self.connection.commit()
            self.connection.close()

            return True
        
        except sqlite3.Error as error:
            logging.info(f"Error into the insert_data_local method: {error}")
            return False


    def insertStatus(self, status: str):
        try:

            self.cursor.execute(f"INSERT INTO status_db (status) VALUES ({status})")

            self.connection.commit()
            self.connection.close()
        except sqlite3.Error as error:
            logging.info(f"Eroare into the insert_status_local method: {error}")


    def delete(self):
        try:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            cursor.execute("DELETE FROM data;")
            logging.info("the local data was deleted successfully")

            connection.commit()
            connection.close()

        except sqlite3.Error as error:
            logging.info(f"Error into the delete_local_data method: {error}")
