"""
File that regroups static method that can be used by all scene objects
"""

from PySide2.QtCore import Qt
from PySide2.QtGui import QPen


def initialize_qpen(qt_color):
    """
    Initializes a Qt QPen with color qt_clor
    :param qt_color: A color from Qt: Qt.Color
    :return: returns the created QPen
    """
    mpen = QPen()
    mpen.setCapStyle(Qt.FlatCap)
    mpen.setWidth(2)
    mpen.setColor(qt_color)

    return mpen
