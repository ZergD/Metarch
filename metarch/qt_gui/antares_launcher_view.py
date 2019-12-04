from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QGraphicsView, QApplication
from PySide2.QtCore import Qt, QPoint


class AntaresLauncherView(QGraphicsView):
    def __init__(self, scene):
        super(AntaresLauncherView, self).__init__(scene=scene)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.verticalScrollBar().setDisabled(True)

        # self.setSceneRect(self.sceneRect())
        self.centerOn(QPoint(740, 390))

        # print("self.sceneRect")
        # print(self.sceneRect())

        self.setRenderHint(QPainter.Antialiasing)


    def keyPressEvent(self, qkey_event):
        if qkey_event.key() == Qt.Key_Q:
            print("Key \"Q\" pressed... Exiting Application...")
            QApplication.instance().quit()

    # def mousePressEvent(self qmouse_event):
    #     QGraphicsView.mousePressEvent(self, qmouse_event)
    #     self.viewport().setCursor(Qt.ArrowCursor)
    #     qpointf = self.mapToScene(qmouse_event.pos())
    #     print("mapToScene : items at position " + str(qpointf.x()) + " y:" + str(qpointf.y()))
