from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplu PyQt5")
        self.setGeometry(100, 100, 1000, 600)

        self.initUI()

    def initUI(self):

        # ------------------------ VARIABLES --------------------------------------------------------------------
        temperature = "Temp"
        humidity = "Hum"
        treshold = "23"
        plus = "+"
        minus = "-"

        # ------------------------- CONTAINERS --------------------------------------------------------------------
        div_home_temp = QWidget(self)
        div_home_temp.setStyleSheet("QWidget { background-color: green; border-radius: 70%; }")
        div_home_temp.setFixedSize(150, 150)
        div_home_temp.move(200, 80)

        div_home_hum = QWidget(self)
        div_home_hum.setStyleSheet("QWidget { background-color: red; border-radius: 70%; }")
        div_home_hum.setFixedSize(150, 150)
        div_home_hum.move(200, 330)

        div_treshold = QWidget(self)
        div_treshold.setStyleSheet("QWidget { background-color: blue; border-radius: 70%; }")
        div_treshold.setFixedSize(150, 150)
        div_treshold.move(550, 220)

        
        div_plus = QWidget(self)
        div_plus.setStyleSheet("QWidget { background-color: yellow; border-radius: 50%; }")
        div_plus.setFixedSize(100, 100)
        div_plus.move(680, 130)

                
        div_minus = QWidget(self)
        div_minus.setStyleSheet("QWidget { background-color: yellow; border-radius: 50%; }")
        div_minus.setFixedSize(100, 100)
        div_minus.move(680, 350)


        # ---------------- LAYOUT CONTAINERS ---------------------------------------------------------------------
        div_home_temp_layout = QVBoxLayout(div_home_temp)
        div_home_temp.setLayout(div_home_temp_layout)

        div_home_hum_layout = QVBoxLayout(div_home_hum)
        div_home_hum.setLayout(div_home_hum_layout)

        div_treshold_layout = QVBoxLayout(div_treshold)
        div_treshold.setLayout(div_treshold_layout)

        div_plus_layout = QVBoxLayout(div_plus)
        div_plus.setLayout(div_plus_layout)

        div_minus_layout = QVBoxLayout(div_minus)
        div_minus.setLayout(div_minus_layout)


        # ------------------------ LABELS -----------------------------------------------------------------------
        home_temp_label = QLabel(temperature, div_home_temp)
        home_temp_label.setStyleSheet(" QLabel { font-size: 30px; }")
        
        home_hum_label = QLabel(humidity, div_home_hum)
        home_hum_label.setStyleSheet(" QLabel { font-size: 30px; }")

        treshold_label = QLabel(treshold, div_treshold)
        treshold_label.setStyleSheet(" QLabel { font-size: 50px; }")

        plus_label = QLabel(plus, div_plus)
        plus_label.setStyleSheet(" QLabel { font-size: 45px; }")
    
        minus_label = QLabel(minus, div_minus)
        minus_label.setStyleSheet(" QLabel { font-size: 45px; }")


        # ---------------- LAYOUTS ADDS --------------------------------------------------------------------------
        div_home_temp_layout.addWidget(home_temp_label)
        div_home_hum_layout.addWidget(home_hum_label)
        div_treshold_layout.addWidget(treshold_label)
        div_plus_layout.addWidget(plus_label)
        div_minus_layout.addWidget(minus_label)


        # ---------------------- CENTER THE LABELS --------------------------------------------------------------
        div_home_temp_layout.setAlignment(Qt.AlignCenter) 
        div_home_hum_layout.setAlignment(Qt.AlignCenter) 
        div_treshold_layout.setAlignment(Qt.AlignCenter) 
        div_plus_layout.setAlignment(Qt.AlignCenter) 
        div_minus_layout.setAlignment(Qt.AlignCenter) 


if __name__ == '__main__':
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())