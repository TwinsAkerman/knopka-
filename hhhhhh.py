# ocnova biblioteki
from PyQt5.QtCore import *
# vidgeti
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

lbl = QLabel("Текст :)")
btn = QPushButton("Кнопка типа")

main_layout = QVBoxLayout()
main_layout.addWidget(lbl)
main_layout.addWidget(btn)

window.setLayout(main_layout)
window.show()
app.exec()