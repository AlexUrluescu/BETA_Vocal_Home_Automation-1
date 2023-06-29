from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplu PyQt5")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        container = QWidget(self)
        layout = QVBoxLayout(container)
        container.setLayout(layout)

        container.setStyleSheet(" QWidget { background-color: red }")

        label1 = QLabel("Text 1")
        label1.setStyleSheet("QLabel { background-color: blue }")

        label2 = QLabel("Text 2")
        label2.setStyleSheet("QLabel { background-color: yellow }")

        cont = QWidget()
        cont.setStyleSheet("QWidget { background-color: green; border-radius: 20px; }")

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(cont)

        self.setCentralWidget(container)

if __name__ == '__main__':
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())