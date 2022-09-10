from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog,QTableWidgetItem,QMainWindow
from src.widget import context
from src.db import config

class Dashboard(QDialog):
    def __init__(self):
        super(Dashboard,self).__init__()
        loadUi("ui/dashboard.ui",self)
  
        self.tableWidget.setColumnWidth(0,250)
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,145)
        self.table_view()

        self.userbutton.setText('current user : '+context['user'])
        self.gotoProductLink.clicked.connect(self.gotoaddproduct)
        self.stock_btn.clicked.connect(self.showchart_by_stock)
        self.product_btn.clicked.connect(self.showchart_by_product)
        self.logoutButton.clicked.connect(self.logout)


        
    from src.widget import widget

    def gotoaddproduct(self):
        from src.views.addProduct import AddProduct
        create=AddProduct()
        self.widget.addWidget(create)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def logout(self):
        from src.views.login import Login
        login = Login()
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)


    def table_view(self):
        products = config.list_product()
        row = 0
        self.tableWidget.setRowCount(len(products))
        for product in products:
            self.tableWidget.setItem(row,0,QTableWidgetItem(product['name']))
            self.tableWidget.setItem(row,1,QTableWidgetItem(product['category']))
            self.tableWidget.setItem(row,2,QTableWidgetItem(str(product['stock'])))
            row+=1
    
    def showchart_by_stock (self):
        from src.views import graph
        self.window =QMainWindow()
        self.ui = graph.Graph1()


    def showchart_by_product (self):
        from src.views import graph
        self.window =QMainWindow()
        self.ui = graph.Graph2()



        





        









    