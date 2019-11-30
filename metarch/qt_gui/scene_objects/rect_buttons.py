from PySide2.QtWidgets import QGraphicsRectItem
from metarch.qt_gui import scene_objects
from PySide2.QtCore import Qt


class RectButton(QGraphicsRectItem):
    def __init__(self, x, y, height, width, text):
        """
        A Rectangle with some text in it
        :param text: str
        :param x: float
        :param y: float
        :param height: float
        :param width: float
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        super(RectButton, self).__init__(self.x, self.y, self.width, self.height)

        self.mpen = scene_objects.initialize_qpen(Qt.gray)

    def paint(self, qpainter, qstyle_option_graphics_item, widget=None):
        qpainter.setPen(self.mpen)
        qpainter.drawRect(self.x, self.y, self.width, self.height)





