from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog
from src.db import config


class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount,self).__init__()
        loadUi("ui/create.ui",self)
        
        self.createButton.clicked.connect(self.createAccountFunction)
        # self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gotoLoginButton.clicked.connect(self.gotoLogin)

    from src.widget import widget
    from src.views.login import Login

    def gotoLogin(self):
        login=self.Login()
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)


    def createAccountFunction(self):     
        username  = self.username.text()
        password  = self.password.text()
        password2 = self.password_2.text() 
        if password==password2:
            config.create_user(id=2,username=username,password=password)
            print("Successfully created account with username: ",username)
            login=self.Login()
            self.widget.addWidget(login)
            self.widget.setCurrentIndex(self.widget.currentIndex()+1)





   
