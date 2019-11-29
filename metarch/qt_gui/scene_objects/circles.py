from PySide2.QtCore import QRectF, Qt, QPoint
from PySide2.QtWidgets import QGraphicsItem

from metarch.qt_gui import scene_objects

GLOBAL_BLOCK_HEIGHT = 10


class Circle(QGraphicsItem):
    """
    pos is a QPoint()
    """

    def __init__(self, pos):
        super(Circle, self).__init__()

        self.length = 30

        self.pos = pos

        self.mpen = scene_objects.initialize_qpen(Qt.yellow)

    def boundingRect(self):
        return QRectF(self.pos.x() - 7, self.pos.y(), GLOBAL_BLOCK_HEIGHT + 6, GLOBAL_BLOCK_HEIGHT + 6)

    def paint(self, qpainter, qstyle_option_graphics_item, widget=None):
        qpainter.setPen(self.mpen)
        # qpainter.drawLine(self.pos, QPoint(self.pos.x() + self.length, self.pos.y() + self.length))
        qpainter.setBrush(self.mpen.color())
        qpainter.drawEllipse(self.pos, self.length, self.length)
