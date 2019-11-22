from abc import ABC, abstractmethod

# Abstract Class
class Chart():
    @abstractmethod
    def display(self):
        pass


class HistogramChart(Chart):
    def __init__(self):
        print('creating HistogramChart')

    def display(self):
        print('display HistogramChart')

class PieChart(Chart):
    def __init__(self):
        print('creating PieChart')

    def display(self):
        print('display PieChart')

class LineChart(Chart):
    def __init__(self):
        print('creating LineChart')

    def display(self):
        print('display LineChart')


class ChartFactory():
    def __init__(self):
        pass

    @staticmethod
    def getChart(type):
        chart = None
        if type == 'histogram':
            chart = HistogramChart()
            print('Initializing HistogramChart')
        elif type == 'pie':
            chart = PieChart()
            print('Initializing PieChart')
        elif type == 'line':
            chart = LineChart()
            print('Initializing LineChart')
        return chart


if __name__ == '__main__':
    chart = ChartFactory.getChart('histogram')
    chart.display()

