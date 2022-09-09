import sys
from PyQt6 import QtWidgets

app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()

context = {
    'user' : None,   
}