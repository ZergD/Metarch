from PySide2.QtWidgets import QMainWindow, QGraphicsView, QVBoxLayout, QWidget

from metarch.qt_gui.antares_launcher_scene import AntaresLauncherScene


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.scene = AntaresLauncherScene()
        self.view = QGraphicsView(self.scene)

        self.layout = QVBoxLayout()

        self.setCentralWidget(self.view)






