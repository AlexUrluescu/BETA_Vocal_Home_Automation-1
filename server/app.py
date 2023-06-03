from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Alex'
app.config['MYSQL_PASSWORD'] = 'gabiurluescu'
app.config['MYSQL_DB'] = 'alex'

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

@app.route('/edit')
def edit_conatct():
    return "Edit contact"

@app.route('/delete')
def delete_conatct():
    return "Delete contact"

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

if __name__ == '__main__':
    app.run(port = 5000, debug = True)