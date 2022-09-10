from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog
from src.db import config

class AddProduct(QDialog):
    def __init__(self):
        super(AddProduct,self).__init__()
        loadUi("ui/add_product.ui",self)
        self.add_button.clicked.connect(self.addproduct)
        CATEGORIES = ('Medicine','Device','Suppliments','Personal Care')
        self.stock.setMinimum(1)
        for category in CATEGORIES:
            self.category.addItem(category)
        self.backButton.clicked.connect(self.gotoback)

    from src.widget import widget

    def addproduct(self):
        name=self.name.text()
        category=self.category.currentText()
        stock=self.stock.value()
        config.add_product(1,name,stock,category)
        self.msg_label.setText(f"Successfully added a product with name  : {name}")
        print("Successfully added a product with name: ",name)

    def gotoback(self):
        from src.views.dashboard import Dashboard
        view=Dashboard()
        self.widget.addWidget(view)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
    


