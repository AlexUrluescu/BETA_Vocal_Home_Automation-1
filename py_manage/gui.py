from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QSlider
import sys
from PyQt5.QtCore import Qt
import requests
import json
from PyQt5.QtCore import QTimer
from senzor import dht_sensor

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplu PyQt5")
        self.setGeometry(100, 100, 1000, 600)

        self.status = ""
        self.treshlod = 0
        self.id_treshold = ""
        self.temperature = ""
        self.humidity = ""
        self.text_alert = "Temperatura a fost actualizata"
        self.val = 30
        self.button_status = True
        self.id_status = ""

        self.senzor = dht_sensor()
        self.temp_senzor = ""
        self.hum_senzor = ""

        self.timer_alert = QTimer()
        self.timer_alert.setInterval(4000)
        self.timer_alert.setSingleShot(True)
        self.timer_alert.timeout.connect(self.activate_alert)

        self.timer10 = QTimer()
        self.timer10.setInterval(4000)
        self.timer10.setSingleShot(True)
        self.timer10.timeout.connect(self.hide_div)

        self.stil_on = """
            QSlider::groove:horizontal {
                background-color: #ddd;
                height: 20px;
                border-radius: 10px;
            }
            
                QSlider::handle:horizontal {
                    background-color: green;
                    width: 25px;
                    margin: -5px 0;
                    border-radius: 12px;
                }
            """
        
        self.stil_off = """
            QSlider::groove:horizontal {
                background-color: #ddd;
                height: 20px;
                border-radius: 10px;
            }
            
                QSlider::handle:horizontal {
                    background-color: red;
                    width: 25px;
                    margin: -5px 0;
                    border-radius: 12px;
                }
            """

        self.status_test = 0

        treshold = ""
        temperature = "Temp"
        humidity = "Hum"
        text_alert = "Alert"


        print(f"status = {self.status}")

        # --------------- SLIDER -------------------------------------------
        self.slider = QSlider(self)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1)
        self.slider.setGeometry(580,100, 100, 20) 
        self.slider.setValue(self.val)
        self.slider.setFixedSize(100, 50)
        self.slider.valueChanged.connect(self.slider_value_changed)

        # ------------------------- BUTTONS ----------------------------------------------------------------------
        self.button_plus = QPushButton('+', self)
        self.button_plus.setGeometry(680, 140, 80, 80)
        self.button_plus.setStyleSheet("QPushButton { width: 50px; height: 50px; border-radius: 40%; background-color: gold; font-size: 45px; font-family: 'Poppins', sans-serif;}")
        self.button_plus.setEnabled(self.button_status)
        self.button_plus.clicked.connect(self.button_plus_clicked)

        self.button_minus = QPushButton('-', self)
        self.button_minus.setGeometry(680, 370, 80, 80)
        self.button_minus.setStyleSheet("QPushButton { width: 50px; height: 50px; border-radius: 40%; background-color: gold; font-size: 45px; font-family: 'Poppins', sans-serif; }")
        self.button_minus.setEnabled(self.button_status)
        self.button_minus.clicked.connect(self.button_minus_clicked)

        # ------------------------ CONTAINERS ---------------------------------
        self.div_treshold = QWidget(self)
        self.div_treshold.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; }")
        self.div_treshold.setFixedSize(150, 150)
        self.div_treshold.move(550, 220)

        self.div_home_temp = QWidget(self)
        self.div_home_temp.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; }")
        self.div_home_temp.setFixedSize(150, 150)
        self.div_home_temp.move(200, 80)

        self.div_home_hum = QWidget(self)
        self.div_home_hum.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; }")
        self.div_home_hum.setFixedSize(150, 150)
        self.div_home_hum.move(200, 330)

        self.div_text_alert = QWidget(self)
        self.div_text_alert.setStyleSheet("QWidget { background-color: green; border-radius: 20px; font-family: 'Poppins', sans-serif; font-size: 10px; }")
        self.div_text_alert.setFixedSize(350, 50)
        self.div_text_alert.move(500, 50)
        self.div_text_alert.hide()


        # ------------------------- LAYOUT CONTAINERS -------------------------
        self.div_treshold_layout = QVBoxLayout(self.div_treshold)
        self.div_treshold.setLayout(self.div_treshold_layout)

        self.div_home_temp_layout = QVBoxLayout(self.div_home_temp)
        self.div_home_temp.setLayout(self.div_home_temp_layout)

        self.div_home_hum_layout = QVBoxLayout(self.div_home_hum)
        self.div_home_hum.setLayout(self.div_home_hum_layout)

        self.div_text_alert_layout = QVBoxLayout(self.div_text_alert)
        self.div_text_alert.setLayout(self.div_text_alert_layout)

        # -------------------------- LABELS -----------------------------------
        self.treshold_label = QLabel(treshold, self.div_treshold)
        self.treshold_label.setStyleSheet(" QLabel { font-size: 50px; border: none; }")
        self.treshold_label.setText(str(self.treshlod))

        self.home_temp_label = QLabel(temperature, self.div_home_temp)
        self.home_temp_label.setStyleSheet(" QLabel { font-size: 40px; }")
        self.home_temp_label.setText(f"{self.temperature} °C")
        
        self.home_hum_label = QLabel(humidity, self.div_home_hum)
        self.home_hum_label.setStyleSheet(" QLabel { font-size: 40px; }")
        self.home_hum_label.setText(f"{self.humidity} %")
        
        self.text_alert_label = QLabel(text_alert, self.div_text_alert)
        self.text_alert_label.setStyleSheet(" QLabel { font-size: 20px; color: white; }")
        self.text_alert_label.setText(f"{self.text_alert}")

        # ------------------------ LAYOUT ADDS ------------------------------
        self.div_treshold_layout.addWidget(self.treshold_label)
        self.div_home_temp_layout.addWidget(self.home_temp_label)
        self.div_home_hum_layout.addWidget(self.home_hum_label)
        self.div_text_alert_layout.addWidget(self.text_alert_label)

        # ------------------------ CENTER THE LABELS ---------------------------
        self.div_treshold_layout.setAlignment(Qt.AlignCenter) 
        self.div_home_temp_layout.setAlignment(Qt.AlignCenter) 
        self.div_home_hum_layout.setAlignment(Qt.AlignCenter)  
        self.div_text_alert_layout.setAlignment(Qt.AlignCenter)  


        self.initUI()
        self.init_timer()

    
    def fetch_status(self):
        print("intra")
        url = "https://smarthome-dowt.onrender.com/heatingstatus"
        print("iasa")

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            print(data[0]["status"])
            self.status = int(data[0]["status"])
            self.id_status = data[0]["_id"]

            if self.status == 1:
                self.button_status = True
            
            else:
                self.button_status = False

            print(self.status)
            print(type(self.status))

        else:
            print("eroare")

    
    def fetch_heatingTemp(self):
        print("intra")
        url = "https://smarthome-dowt.onrender.com/heatingtemp"
        print("iasa")

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            print(data[0]["temperature"])
            self.treshlod = int(data[0]["temperature"])
            self.id_treshold = data[0]["_id"]
            print(f"treshold = {self.treshlod}")
            print(f"id_treshold: {self.id_treshold}")
            self.treshold_label.setText(str(self.treshlod))


            # print(self.treshlod)
            # print(type(self.treshlod))

        else:
            print("eroare")

    
    def fetch_dataSenzors(self):
        print("intra")
        url = "https://smarthome-dowt.onrender.com/datasenzors"
        print("iasa")

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            print(data[-1])
            print(data[-1]["temperature"])
            print(data[-1]["humidity"])
            self.temperature = str(data[-1]["temperature"])
            self.humidity = str(data[-1]["humidity"])

        else:
            print("eroare")


    def initUI(self):
        print("intra imagine")
        self.setStyleSheet("background-color: rgb(12, 74, 110);")

        # ------------------------ VARIABLES --------------------------------------------------------------------

        if(self.status == 1):
            self.slider.setValue(1)
            self.slider.setStyleSheet(self.stil_on)

        else:
            self.slider.setValue(0)
            self.slider.setStyleSheet(self.stil_off)

        # -------------------------- SLIDER -------------------------------------
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(1)
        slider.setValue(30)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setFixedSize(100, 50)
        slider.move(300, 300)


    def hide_div(self):
        print("hide")
        self.div_text_alert.hide()


    def activate_alert(self):
        self.timer10.start()

        print("shoot")
        self.div_text_alert.show()

        payload = {'temperature': self.treshlod}
        json_payload = json.dumps(payload)
        url = f"https://smarthome-dowt.onrender.com/changeheatingtemp/{self.id_treshold}"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, headers=headers, data=json_payload)
        
        if response.status_code == 200:
            print(response.text)
        else:
           print(f"Eroare ({response.status_code}): {response.text}")        
        

    def button_plus_clicked(self):
        print('plus')
        # print(self.test_tresh)
        print(type(self.treshlod))
        print(self.treshlod)
  
        self.timer_alert.stop()
        self.timer_alert.start()

        self.treshlod = self.treshlod + 0.5
        self.treshold_label.setText(str(self.treshlod))

        # print(type(self.temperature))

        if(self.treshlod > int(self.temperature)):
            print("Ai depasit valoarea din casa")
            self.div_treshold.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; border: 8px solid gold; }")


    def button_minus_clicked(self):
        print("minus")

        self.timer_alert.stop()
        self.timer_alert.start()

        self.treshlod = self.treshlod - 0.5
        self.treshold_label.setText(str(self.treshlod))

        
        if(self.treshlod < int(self.temperature)):
            print("Ai depasit valoarea din casa")
            self.div_treshold.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; border: none; }")
            

    def init_timer(self):
        print("timer")
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_data_senzors)
        self.timer.start(5000)


    def get_data_senzors(self):
        self.temp_senzor = self.senzor.get_t()
        self.home_temp_label.setText(f"{self.temp_senzor} °C")

        self.hum_senzor = self.senzor.get_h()
        self.home_hum_label.setText(f"{self.hum_senzor} %")
        print(f"temp: {self.temp_senzor}")
        print(f"hum: {self.hum_senzor}")


    def slider_value_changed(self, value):
        if(value == 0):
            print("off")
            print(f"Value pe off: {value}")

            self.slider.setStyleSheet(self.stil_off)
            # print(self.button_status)
            self.button_status = False
            self.button_plus.setEnabled(self.button_status)
            self.button_minus.setEnabled(self.button_status)

            payload = {'status': 0}
            json_payload = json.dumps(payload)
            url = f"https://smarthome-dowt.onrender.com/test/{self.id_status}"
            headers = {'Content-Type': 'application/json'}
            response = requests.put(url, headers=headers, data=json_payload)
            
            if response.status_code == 200:
                print(response.text)
            else:
                print(f"Eroare ({response.status_code}): {response.text}")

            # print(self.button_status)
            # print(self.test_status)

        
        else:
            print("on")
            print(f"Value pe on: {value}")
            self.slider.setStyleSheet(self.stil_on)
            # print(self.button_status)
            self.button_status = True
            self.button_plus.setEnabled(self.button_status)
            self.button_minus.setEnabled(self.button_status)

            payload = {'status': 1}
            json_payload = json.dumps(payload)
            url = f"https://smarthome-dowt.onrender.com/test/{self.id_status}"
            headers = {'Content-Type': 'application/json'}
            response = requests.put(url, headers=headers, data=json_payload)
            
            if response.status_code == 200:
                print(response.text)
            else:
                print(f"Eroare ({response.status_code}): {response.text}")

            # print(self.button_status)
            # print(self.test_status)


if __name__ == '__main__':
    
    window = MainWindow()
    window.fetch_status()
    window.fetch_heatingTemp()
    window.fetch_dataSenzors()
    window.initUI()
    window.show()

    sys.exit(app.exec_())