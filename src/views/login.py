from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog
from src.db import config
from src.widget import context

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("ui/login.ui",self)
        self.login_button.clicked.connect(self.loginfunction)
        self.createLink.clicked.connect(self.gotocreate)

    from src.widget import widget

    def gotocreate(self):
        from src.views.createAcoount import CreateAccount
        create=CreateAccount()
        self.widget.addWidget(create)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def loginfunction(self):
        
        username=self.username.text()
        password=self.password.text()
        user=config.find_user(username=username,password=password)

        if user:
            context['user'] = user['username']
            from src.views.dashboard import Dashboard
            dashboard=Dashboard()
            self.widget.addWidget(dashboard)
            self.widget.setCurrentIndex(self.widget.currentIndex()+1)
            print('Current user : ', user['username'])

        else:
            print('invalid credentials')


