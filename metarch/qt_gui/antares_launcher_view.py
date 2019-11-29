from PySide2.QtWidgets import QGraphicsView, QApplication
from PySide2.QtCore import Qt


class AntaresLauncherView(QGraphicsView):
    def __init__(self, scene):
        super(AntaresLauncherView, self).__init__(scene=scene)

    def keyPressEvent(self, qkey_event):
        if qkey_event.key() == Qt.Key_Q:
            print("Key \"Q\" pressed... Exiting Application...")
            QApplication.instance().quit()





