import pymongo

from senzor import dht_sensor

senzor = dht_sensor()

conn = "mongodb+srv://flaviu:parola@cluster0.kzya4z8.mongodb.net/?retryWrites=true&w=majority"

try:
    client = pymongo.MongoClient(conn)

    db = client.mongodb
    colection = db.datasenzors

    documents = colection.find()

    for document in documents:
        data = document


    print(data)
    print(data["temperature"])
    print(data["humidity"])
    print(data["date"])

    temp = senzor.get_t()
    hum = senzor.get_h()

    print(temp)
    print(hum)

    doc = {
        "temperature": temp,
        "humidity": hum,
        "date": "2023-06-25",
    }

    rezultat = colection.insert_one(doc)

    print("ID-ul documentului inserat:", rezultat.inserted_id)

    client.close()

except Exception:
    print("Error " + Exception)

