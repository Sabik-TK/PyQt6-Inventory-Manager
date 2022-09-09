import sys
from PyQt6.QtWidgets import QApplication
from src.views.login import Login
from src.widget import widget

app=QApplication(sys.argv)
widget=widget
mainwindow=Login()
widget.addWidget(mainwindow)
widget.setFixedWidth(720)
widget.setFixedHeight(480)
widget.show()
app.exec()