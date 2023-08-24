from datetime import datetime
from time import sleep
import sqlite3

def create_table():
    conn = sqlite3.connect('weather_data.db') # Conexiunea la baza de date (se creează dacă nu există)
    cursor = conn.cursor()

    # Creează tabela 'weather' cu cele trei coloane: temperatura, umiditate și data
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                        temperatura REAL,
                        umiditate REAL,
                        data TEXT
                    )''')

    conn.commit() # Salvează modificările
    conn.close()  # Închide conexiunea

temperatura = 20
umiditate = 80


def insert_data(temperatura, umiditate):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # Obține data curentă și convert-o la formatul dorit (YYYY-MM-DD)
    data_curenta = datetime.now().strftime('%Y-%m-%d')


    # Inserează datele în tabela 'weather'
    cursor.execute('INSERT INTO weather (temperatura, umiditate, data) VALUES (?, ?, ?)',
                   (temperatura, umiditate, data_curenta))

    conn.commit()
    conn.close()


while True:
    create_table()
    insert_data(temperatura, umiditate)
    sleep(3)