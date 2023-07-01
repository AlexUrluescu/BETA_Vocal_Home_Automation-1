from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
import sys
from PyQt5.QtCore import Qt
import requests

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplu PyQt5")
        self.setGeometry(100, 100, 1000, 600)

        self.status = 0
        self.treshlod = ""
        self.temperature = ""
        self.humidity = ""
        self.val = 0

        treshold = ""


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
            print(self.status)
            print(type(self.status))

        else:
            # self.label.setText('Eroare la preluarea datelor API')
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
            # self.label.setText('Eroare la preluarea datelor API')
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
            # self.treshlod = str(data[0]["temperature"])
            # print(self.treshlod)
            # print(type(self.treshlod))

        else:
            # self.label.setText('Eroare la preluarea datelor API')
            print("eroare")


    def initUI(self):
        print("intra imagine")

        # ------------------------ VARIABLES --------------------------------------------------------------------
        temperature = "Temp"
        humidity = "Hum"
        treshold = "23"
        # plus = "+"
        # minus = "-"


        # ------------------------- BUTTONS ----------------------------------------------------------------------
        
        button_plus = QPushButton('+', self)
        button_plus.setGeometry(680, 130, 100, 100)
        # button.setFixedSize(300, 50)
        button_plus.setStyleSheet("QPushButton { width: 50px; height: 50px; border-radius: 50%; background-color: blue; font-size: 45px; }")

        # Atribuirea funcției button_clicked la evenimentul de apăsare al butonului
        button_plus.clicked.connect(self.button_plus_clicked)


        button_minus = QPushButton('-', self)
        button_minus.setGeometry(680, 350, 100, 100)
        # button.setFixedSize(300, 50)
        button_minus.setStyleSheet("QPushButton { width: 50px; height: 50px; border-radius: 50%; background-color: blue; font-size: 45px; }")

        # Atribuirea funcției button_clicked la evenimentul de apăsare al butonului
        button_minus.clicked.connect(self.button_minus_clicked)


        # ------------------------- CONTAINERS --------------------------------------------------------------------
        div_home_temp = QWidget(self)
        div_home_temp.setStyleSheet("QWidget { background-color: green; border-radius: 70%; }")
        div_home_temp.setFixedSize(150, 150)
        div_home_temp.move(200, 80)

        div_home_hum = QWidget(self)
        div_home_hum.setStyleSheet("QWidget { background-color: red; border-radius: 70%; }")
        div_home_hum.setFixedSize(150, 150)
        div_home_hum.move(200, 330)


        self.div_treshold.setStyleSheet("QWidget { background-color: blue; border-radius: 70%; }")
        self.div_treshold.setFixedSize(150, 150)
        self.div_treshold.move(550, 220)

        
        # div_plus = QWidget(self)
        # div_plus.setStyleSheet("QWidget { background-color: yellow; border-radius: 50%; }")
        # div_plus.setFixedSize(100, 100)
        # div_plus.move(680, 130)

                
        # div_minus = QWidget(self)
        # div_minus.setStyleSheet("QWidget { background-color: yellow; border-radius: 50%; }")
        # div_minus.setFixedSize(100, 100)
        # div_minus.move(680, 350)

        
        div_status = QWidget(self)
        if(self.status == 0):
            div_status.setStyleSheet("QWidget { background-color: red; border-radius: 50%; }")
        
        else:
            div_status.setStyleSheet("QWidget { background-color: green; border-radius: 50%; }")

        div_status.setFixedSize(100, 100)
        div_status.move(800, 200)

        # ---------------- LAYOUT CONTAINERS ---------------------------------------------------------------------
        div_home_temp_layout = QVBoxLayout(div_home_temp)
        div_home_temp.setLayout(div_home_temp_layout)

        div_home_hum_layout = QVBoxLayout(div_home_hum)
        div_home_hum.setLayout(div_home_hum_layout)


        # div_plus_layout = QVBoxLayout(div_plus)
        # div_plus.setLayout(div_plus_layout)

        # div_minus_layout = QVBoxLayout(div_minus)
        # div_minus.setLayout(div_minus_layout)

        div_status_layout = QVBoxLayout(div_status)
        div_status.setLayout(div_status_layout)

        # ------------------------ LABELS -----------------------------------------------------------------------
        home_temp_label = QLabel(temperature, div_home_temp)
        home_temp_label.setStyleSheet(" QLabel { font-size: 30px; }")
        home_temp_label.setText(self.temperature)
        
        home_hum_label = QLabel(humidity, div_home_hum)
        home_hum_label.setStyleSheet(" QLabel { font-size: 30px; }")
        home_hum_label.setText(self.humidity)


        self.treshold_label.setStyleSheet(" QLabel { font-size: 50px; }")
        self.treshold_label.setText(str(self.val))

        # plus_label = QLabel(plus, div_plus)
        # plus_label.setStyleSheet(" QLabel { font-size: 45px; }")
    
        # minus_label = QLabel(minus, div_minus)
        # minus_label.setStyleSheet(" QLabel { font-size: 45px; }")

        if(self.status == 0):
            status_label = QLabel("Off", div_status)
            status_label.setStyleSheet(" QLabel { font-size: 35px; }")

        else:
            status_label = QLabel("On", div_status)
            status_label.setStyleSheet(" QLabel { font-size: 35px; }")


        # ---------------- LAYOUTS ADDS --------------------------------------------------------------------------
        div_home_temp_layout.addWidget(home_temp_label)
        div_home_hum_layout.addWidget(home_hum_label)
        # div_plus_layout.addWidget(plus_label)
        # div_minus_layout.addWidget(minus_label)
        div_status_layout.addWidget(status_label)

        # ---------------------- CENTER THE LABELS --------------------------------------------------------------
        div_home_temp_layout.setAlignment(Qt.AlignCenter) 
        div_home_hum_layout.setAlignment(Qt.AlignCenter) 
        # div_plus_layout.setAlignment(Qt.AlignCenter) 
        # div_minus_layout.setAlignment(Qt.AlignCenter) 
        div_status_layout.setAlignment(Qt.AlignCenter) 


    def button_plus_clicked(self):
        print('plus')
        print(self.val)
        self.val = self.val + 1
        print(self.val)
        self.treshold_label.setText(str(self.val))


    def button_minus_clicked(self):
        print("minus")
        self.val = self.val - 1
        self.treshold_label.setText(str(self.val))



if __name__ == '__main__':
    
    window = MainWindow()
    # window.fetch_status()
    # window.fetch_heatingTemp()
    # window.fetch_dataSenzors()
    window.initUI()
    window.show()

    sys.exit(app.exec_())