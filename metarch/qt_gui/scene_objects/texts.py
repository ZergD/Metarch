from PySide2.QtGui import QColor, QFont
from PySide2.QtWidgets import QGraphicsTextItem
from PySide2.QtCore import Qt


class HText(QGraphicsTextItem):
    def __init__(self, text, x, y, parent, font=3):
        if parent is None:
            raise ValueError("Htext error, parent == None")

        # self.orangeColor = QColor(255, 165, 0)
        self.orangeColor = Qt.white
        self.x = int(x)
        # self.x = int((int(x) / 100) * global_mainLine_offset)
        self.y = int(y)
        self.text = text
        self.font = font

        super().__init__(text)
        self.setParentItem(parent)
        self.setFont(QFont("Times", font))
        self.setPos(self.x, self.y)
        self.setDefaultTextColor(self.orangeColor)
        # self.setAcceptHoverEvents(True)
        self.setZValue(9)

        self.parent = None

    def hoverEnterEvent(self, event):
        # print("you hovered !!!")
        self.setDefaultTextColor(Qt.white)
        self.update()

    def hoverLeaveEvent(self, event):
        self.setDefaultTextColor(self.orangeColor)
        self.update()

    def mousePressEvent(self, qmouse_event):
        self.parent = self.parentItem()
        print("you pressed on Htext with name = " + str(self.text))
        # print("this item has " + str(len(self.parents)) + " parents")
        if self.parent:
            print(self.parent)
            # if isinstance(self.parent, Signal):
            #    self.parent.mousePressEvent(QMouseEvent)
            # else:
            #    self.parent.mousePressEvent(QMouseEvent)

    def to_string(self):
        print("HText: " + self.text + " at position x:" + str(self.x) + " y: " + str(self.y))
