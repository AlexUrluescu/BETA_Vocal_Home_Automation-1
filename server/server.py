from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'parola'
app.config['MYSQL_DB'] = 'flaviu'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods = ['POST'])
def add_conatct():
    if request.method == 'POST':
        temperature = request.form['temperature']
        humidity = request.form['humidity']
        date = request.form['date']

        print(temperature)
        print(humidity)
        print(date)

        cursor = mysql.connection.cursor()

        cursor.execute(f"INSERT INTO data_senzori (temperature, humidity, date) VALUES ({temperature}, {humidity}, '2023-06-10')")

        mysql.connection.commit()

        return "received"


@app.route('/get_data')
def get_data():
    cursor = mysql.connection.cursor()

    cursor.execute(f"SELECT * FROM data_senzori")

    rows = cursor.fetchall()
    data = []

    # Parcurge fiecare rând și adaugă-l în lista de dicționare
    for row in rows:
        # Creează un dicționar pentru fiecare rând
        row_dict = {
            'id': row[0],
            'temperature': row[1],
            'humidity': row[2],
            'date': row[3],
            # Adaugă aici și alte coloane din tabel
        }
        data.append(row_dict)

    mysql.connection.commit()

    return jsonify(data)

@app.route('/get_status')
def get_status():
    cursor = mysql.connection.cursor()

    cursor.execute(f"SELECT * FROM heating_status")

    rows = cursor.fetchall()

    for row in rows:
        row_dict = row[1]
        data = row_dict

    mysql.connection.commit()

    return jsonify(data)


@app.route('/turn_on_status', methods = ['POST'])
def turn_on_status():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()

        cursor.execute(f"""
                    UPDATE heating_status SET status = 1 WHERE id = 1
                    """)
        mysql.connection.commit()

        return jsonify({"stare": "on", "status": 1})
    

@app.route('/turn_off_status', methods = ['POST'])
def turn_off_status():
    if request.method == 'POST':         
        cursor = mysql.connection.cursor()

        cursor.execute(f"""
                    UPDATE heating_status SET status = 0 WHERE id = 1
                    """)
        mysql.connection.commit()

        return jsonify({"stare": "on", "status": 0})



@app.route('/get_heating_temp')
def get_heating_temp():
    cursor = mysql.connection.cursor()

    cursor.execute(f"SELECT * FROM heating_temp")

    rows = cursor.fetchall()

    for row in rows:
        row_dict = row[1]
        data = row_dict

    mysql.connection.commit()

    return jsonify(data)


@app.route('/get_recent_temp')
def get_recent_temp():
    cursor = mysql.connection.cursor()

    cursor.execute(f"SELECT * FROM data_senzori WHERE id = (SELECT MAX(id) FROM data_senzori)")

    rows = cursor.fetchall()

    data = []

    for row in rows:
        row_dict = {
            "temperature": row[1],
            "humidity": row[2],
        }

        data.append(row_dict)

    mysql.connection.commit()

    return jsonify(row_dict)


@app.route('/test')
@cross_origin()
def test():
    data = {
        "nume": 'Alex'
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host = "192.168.1.101", port = 5000, debug = True)