from math import pi
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton

def input_radius():
    global radius
    radius = float(inputline.text())

def find_perimeter():
    global displaytext
    displaytext += ("The perimeter of the circle is " + str(2.0 * pi * radius) + 'cm\n')
    display.setText(displaytext)

def find_area():
    global displaytext
    displaytext += ("The area of the circle is " + str(pi * pow(radius, 2)) + 'cm\n')
    display.setText(displaytext)

app = QApplication([])
w = QWidget()
w.setWindowTitle('Geometry calculator for circles')
w.resize(800, 500)
display = QTextEdit()
inputline = QLineEdit()
inputline.setPlaceholderText('type here:')
pb1 = QPushButton('input radius in cm')
pb2 = QPushButton("find perimeter")
pb3 = QPushButton('find area')
displaytext = ''
widgets_to_add_to_lv1 = [pb1, pb2, pb3, inputline]
lv1 = QVBoxLayout()
lh1 = QHBoxLayout()
for i in widgets_to_add_to_lv1:
    lv1.addWidget(i)
lh1.addWidget(display)
lh1.addLayout(lv1)
w.setLayout(lh1)
w.show()
pb1.clicked.connect(input_radius)
pb2.clicked.connect(find_perimeter)
pb3.clicked.connect(find_area)
app.exec_()