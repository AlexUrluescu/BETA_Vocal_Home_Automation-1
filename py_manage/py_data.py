import pymongo

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

    client.close()

except Exception:
    print("Error " + Exception)

