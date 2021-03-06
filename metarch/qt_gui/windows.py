from pathlib import Path

from PySide2.QtCore import Qt
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QProgressBar

from metarch.qt_gui.antares_launcher_scene import AntaresLauncherScene
from metarch.qt_gui.antares_launcher_view import AntaresLauncherView


class MainWindow(QMainWindow):
    # ## resize(QGuiApplication::primaryScreen()->availableSize() * 3 / 5); TO ABSOLUTELY EFING TEST !!!!
    def __init__(self):
        super(MainWindow, self).__init__()

        self.top_header = self.create_top_header_qlabel()

        self.progress_bar = self.init_progress_bar()

        self.scene = AntaresLauncherScene(self.progress_bar)
        self.view = AntaresLauncherView(self.scene)
        self.view2 = AntaresLauncherView(self.scene)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.top_header)
        self.layout.addWidget(self.view)
        # self.layout.addWidget(self.progress_bar.setContentsMargins(5, 5, 5, 5))
        self.layout.addWidget(self.progress_bar)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        main_body_widget = QWidget()
        main_body_widget.setLayout(self.layout)

        self.setCentralWidget(main_body_widget)

        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.MSWindowsFixedSizeDialogHint)

        self.setWindowTitle("Antares Launcher")

    @staticmethod
    def init_progress_bar():
        qprogress_bar = QProgressBar()
        qprogress_bar.setMinimum(0)
        qprogress_bar.setMaximum(5)
        qprogress_bar.setValue(0)

        return qprogress_bar

    @staticmethod
    def create_top_header_qlabel():
        qlabel = QLabel()
        path = Path.cwd() / "metarch/ressources/antares_header_05.png"
        print("is file = ", path.is_file())
        print("path = ", path)
        if path.is_file():
            image = QImage(str(path))
            print("image = ", image)
            print("images height = ", image.height())
            qpixmap = QPixmap(image)

            qlabel.setPixmap(qpixmap)
            # qlabel.setGeometry(0, 0, 809, 359)

            return qlabel

        else:
            print("ERROR ! Cannot find file for QImage")
            return None
