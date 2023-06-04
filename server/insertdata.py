import random
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Alex",
  password="gabiurluescu",
  database="alex"
)


def insertData():
    temp_rand = random.randint(10,40)
    hum_rand = random.randint(40, 90)

    print(temp_rand)
    print(hum_rand)
    cursor = mydb.cursor()

    
    cursor.execute(f"INSERT INTO data_senzori (temperature, humidity, date) VALUES ({temp_rand}, {hum_rand}, '2023-06-10')")

    mydb.commit()

    print("succefully")


def timer_insert():
    while True:
        insertData()
        time.sleep(10)

timer_insert()