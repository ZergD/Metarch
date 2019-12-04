from PySide2.QtWidgets import QMainWindow, QGraphicsView, QVBoxLayout, QWidget
from PySide2.QtCore import Qt

from metarch.qt_gui.antares_launcher_scene import AntaresLauncherScene
from metarch.qt_gui.antares_launcher_view import AntaresLauncherView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.top_header = QWidget()
        self.scene = AntaresLauncherScene()
        self.view = AntaresLauncherView(self.scene)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.top_header)
        self.layout.addWidget(self.view)

        main_body_widget = QWidget()
        main_body_widget.setLayout(self.layout)

        self.setCentralWidget(main_body_widget)

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)




