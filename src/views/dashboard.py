from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog
from src.widget import context


class Dashboard(QDialog):
    def __init__(self):
        super(Dashboard,self).__init__()
        loadUi("ui/dashboard.ui",self)
        self.userbutton.setText('current user : '+context['user'])
        self.gotoProductLink.clicked.connect(self.gotoaddproduct)
        
    from src.widget import widget
    def gotoaddproduct(self):
        from src.views.addProduct import AddProduct
        create=AddProduct()
        self.widget.addWidget(create)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

