from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtCore import Qt


class AntaresLauncherScene(QGraphicsScene):

    def __init__(self):
        super(AntaresLauncherScene, self).__init__()

        self.setBackgroundBrush(Qt.black)


