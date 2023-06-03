from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(port = 3000, debug = True)