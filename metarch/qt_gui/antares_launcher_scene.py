from PySide2.QtCore import Qt, QPoint
from PySide2.QtWidgets import QGraphicsScene

from metarch.qt_gui.scene_objects.circles import Circle


class AntaresLauncherScene(QGraphicsScene):

    def __init__(self):
        super(AntaresLauncherScene, self).__init__()

        self.setBackgroundBrush(Qt.black)
        # self.setSceneRect(-1000, -1000, 2000, 2000)
        self.setSceneRect(-500, -500, 1000, 1000)

        self.addItem(Circle(QPoint(10, 10)))
