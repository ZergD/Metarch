from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView
# from PySide2.


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)


