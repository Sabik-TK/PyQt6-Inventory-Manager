from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCharts import QChart,QChartView,QPieSeries
from src.db import config

class Graph1(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Category Graph')
        self.setGeometry(100,100,600,600)
        self.chart_view()
        self.show()


    def chart_view(self):

        series = QPieSeries()
        results=config.cursor.execute(f"SELECT category,sum(stock) from Product GROUP BY category")
        for result in results:
            series.append(result[0],result[1])
        
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTitle('Stock Reoprt')

        chartview = QChartView(chart)
        self.setCentralWidget(chartview)

class Graph2(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Category Graph')
        self.setGeometry(100,100,600,600)
        self.chart_view()
        self.show()


    def chart_view(self):

        series = QPieSeries()
        series.setHoleSize(0.4  )
        results=config.cursor.execute(f"SELECT category,count(stock) from Product GROUP BY category")
        for result in results:
            series.append(result[0],result[1])
        
        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTitle('Product Count Reoprt')

        chartview = QChartView(chart)
        self.setCentralWidget(chartview)
