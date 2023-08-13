from math import pi
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton

def input_radius():
    global radius
    global calculateperimeter
    global calculatearea
    try:
        radiusprevious = radius
    except:
        pass
    radius = float(inputline.text())
    inputline.clear()
    try:
        if radiusprevious != radius:
            calculateperimeter = True
            calculatearea = True
    except:
        pass

def find_perimeter():
    global displaytext
    global calculateperimeter 
    if calculateperimeter:   
        displaytext += ("The perimeter of the circle is " + str(2.0 * pi * radius) + 'cm\n')
        display.setText(displaytext)
        calculateperimeter = False

def find_area():
    global displaytext
    global calculatearea
    if calculatearea:
        displaytext += ("The area of the circle is " + str(pi * pow(radius, 2)) + ' square centimetres\n')
        display.setText(displaytext)
        calculatearea = False

app = QApplication([])
w = QWidget()
w.setWindowTitle('Geometry calculator for circles')
w.resize(800, 500)
display = QTextEdit()
display.setReadOnly(True)
inputline = QLineEdit()
inputline.setPlaceholderText('type here:')
pb1 = QPushButton('input radius in cm')
pb2 = QPushButton("find perimeter")
pb3 = QPushButton('find area')
displaytext = ''
calculateperimeter = True
calculatearea = True
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
app.exec()