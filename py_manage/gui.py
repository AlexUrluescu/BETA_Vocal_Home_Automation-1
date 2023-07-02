from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QSlider
import sys
from PyQt5.QtCore import Qt
import requests

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplu PyQt5")
        self.setGeometry(100, 100, 1000, 600)

        self.status = ""
        self.treshlod = ""
        self.temperature = ""
        self.humidity = ""
        self.val = 30
        self.button_status = True

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


        # ------------------------- LAYOUT CONTAINERS -------------------------
        self.div_treshold_layout = QVBoxLayout(self.div_treshold)
        self.div_treshold.setLayout(self.div_treshold_layout)

        # -------------------------- LABELS -----------------------------------
        self.treshold_label = QLabel(treshold, self.div_treshold)


        # ------------------------ LAYOUT ADDS ------------------------------
        self.div_treshold_layout.addWidget(self.treshold_label)


        # ------------------------ CENTER THE LABELS ---------------------------
        self.div_treshold_layout.setAlignment(Qt.AlignCenter) 


        self.initUI()

    
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
            self.treshlod = str(data[0]["temperature"])
            print(self.treshlod)
            print(type(self.treshlod))

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
        temperature = "Temp"
        humidity = "Hum"

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

        # ------------------------- CONTAINERS --------------------------------------------------------------------
        div_home_temp = QWidget(self)
        div_home_temp.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; }")
        div_home_temp.setFixedSize(150, 150)
        div_home_temp.move(200, 80)

        div_home_hum = QWidget(self)
        div_home_hum.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; }")
        div_home_hum.setFixedSize(150, 150)
        div_home_hum.move(200, 330)

        self.div_treshold.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; }")
        self.div_treshold.setFixedSize(150, 150)
        self.div_treshold.move(550, 220)

        # ---------------- LAYOUT CONTAINERS ---------------------------------------------------------------------
        div_home_temp_layout = QVBoxLayout(div_home_temp)
        div_home_temp.setLayout(div_home_temp_layout)

        div_home_hum_layout = QVBoxLayout(div_home_hum)
        div_home_hum.setLayout(div_home_hum_layout)

        # ------------------------ LABELS -----------------------------------------------------------------------
        home_temp_label = QLabel(temperature, div_home_temp)
        home_temp_label.setStyleSheet(" QLabel { font-size: 40px; }")
        home_temp_label.setText(f"{self.temperature} °C")
        
        home_hum_label = QLabel(humidity, div_home_hum)
        home_hum_label.setStyleSheet(" QLabel { font-size: 40px; }")
        home_hum_label.setText(f"{self.humidity} %")


        self.treshold_label.setStyleSheet(" QLabel { font-size: 50px; border: none; }")
        self.treshold_label.setText(str(self.val))

        # ---------------- LAYOUTS ADDS --------------------------------------------------------------------------
        div_home_temp_layout.addWidget(home_temp_label)
        div_home_hum_layout.addWidget(home_hum_label)

        # ---------------------- CENTER THE LABELS --------------------------------------------------------------
        div_home_temp_layout.setAlignment(Qt.AlignCenter) 
        div_home_hum_layout.setAlignment(Qt.AlignCenter)  


    def button_plus_clicked(self):
        print('plus')
        self.val = self.val + 0.5
        self.treshold_label.setText(str(self.val))

        print(type(self.val))
        print(type(self.temperature))

        if(self.val > int(self.temperature)):
            print("Ai depasit valoarea din casa")
            self.div_treshold.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; border: 8px solid gold; }")


    def button_minus_clicked(self):
        print("minus")
        self.val = self.val - 0.5
        self.treshold_label.setText(str(self.val))

        
        if(self.val < int(self.temperature)):
            print("Ai depasit valoarea din casa")
            self.div_treshold.setStyleSheet("QWidget { background-color: white; border-radius: 75%; font-family: 'Poppins', sans-serif; border: none; }")
            

    def slider_value_changed(self, value):
        if(value == 0):
            print("off")
            self.slider.setStyleSheet(self.stil_off)
            # print(self.button_status)
            self.button_status = False
            self.button_plus.setEnabled(self.button_status)
            self.button_minus.setEnabled(self.button_status)
            # print(self.button_status)
            # print(self.test_status)

        
        else:
            print("on")
            self.slider.setStyleSheet(self.stil_on)
            # print(self.button_status)
            self.button_status = True
            self.button_plus.setEnabled(self.button_status)
            self.button_minus.setEnabled(self.button_status)
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