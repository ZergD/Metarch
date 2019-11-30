"""
File that regroups static method that can be used by all scene objects
"""

from PySide2.QtCore import Qt, QPointF
from PySide2.QtGui import QPen
from PySide2.QtWidgets import QGraphicsLineItem


def initialize_qpen(qt_color, width=2):
    """
    Initializes a Qt QPen with color qt_clor
    :param width:
    :param qt_color: A color from Qt: Qt.Color
    :return: returns the created QPen
    """
    mpen = QPen()
    mpen.setCapStyle(Qt.FlatCap)
    mpen.setWidth(width)
    mpen.setColor(qt_color)

    return mpen


def init_visual_scene_axis():
    """
    Create two lines that represent the axis of the scene
    :return: the two Items that are the lines
    """
    # axis.append(QGraphicsLineItem(QPointF(-500, 0), QPointF(500, 0)))
    # axis.append(QGraphicsLineItem(QPointF(0, 500), QPointF(0, -500)))

    hor_line = QGraphicsLineItem(-500, 0, 500, 0)
    hor_line.setPen(initialize_qpen(Qt.green, 1))

    vert_line = QGraphicsLineItem(0, 500, 0, -500)
    vert_line.setPen(initialize_qpen(Qt.green, 1))

    return [hor_line, vert_line]
