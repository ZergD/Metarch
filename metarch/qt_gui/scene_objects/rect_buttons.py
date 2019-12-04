import numpy as np
from PySide2.QtCore import Qt, QRectF, Signal, QObject
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QGraphicsRectItem, QGraphicsItem, QFileDialog

from metarch.qt_gui import scene_objects
from pathlib import Path
import os

from metarch.qt_gui.scene_objects.texts import HText


class RectButton(QGraphicsRectItem):
    ID = 0

    def __init__(self, x, y, width, height, text):
        """
        A Rectangle with some text in it
        :param text: str
        :param x: float
        :param y: float
        :param height: float
        :param width: float
        """
        self.id = RectButton.ID
        RectButton.ID += 1
        # print("my self.id = ", str(self.id))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        super(RectButton, self).__init__(self.x, self.y, self.width, self.height)

        # simple state array, represented as a numpy array, 0 = False, 1 = True
        # [0] = ZIPPED, [1] = SENT, [2] = SUBMITTED, [3] = FINISHED, [4] = DELIVERED
        self.state = np.zeros(5)
        self.state[0] = 1
        # print(self.state.any())
        # indexes = np.array(np.where(self.state == 1))
        # indexes = list(np.where(self.state == 1))
        indexes = np.where(self.state == 1)

        # print("state = \n", self.state)

        self.mpen = scene_objects.initialize_qpen(Qt.gray)
        self.current_color = Qt.gray
        self.current_color_1 = Qt.gray
        self.current_color_2 = Qt.gray
        self.i = 0
        # print("################################################################################\n")
        self.qfile_name = QFileDialog()

    def mousePressEvent(self, q_mouse_event):
        # parent = self.parentItem()
        # parent.mousePressEvent(q_mouse_event)

        if self.id == 0:
            # print("we create a QFileDialog")
            # qfile_name = QFileDialog().getOpenFileName("Choose a Simulation Folder", str(Path.cwd()))
            qfile_name = self.qfile_name.getExistingDirectory()
            # print("get existing directory : ", QFileDialog().getExistingDirectory())
            # qfile_name = QFileDialog().getOpenFileName()
            print("You choose the file directory: ", qfile_name)
            self.id += 1

        self.i = (self.i + 1) % 2
        print("self.i = ", self.i)

        self.state = np.zeros(5)
        self.state[self.i] = 1

        self.update()

        # print("you pressed on RectButton with name = " + str(self.text))
        # # print("this item has " + str(len(self.parents)) + " parents")
        # if self.parent:
        #     print(self.parent)
        #     if isinstance(self.parent, Signal):
        #         self.parent.mousePressEvent(q_mouse_event)
        #     else:
        #         self.parent.mousePressEvent(q_mouse_event)

    def boundingRect(self):
        offset = 0.5
        # return QRectF(self.x - offset, self.y - offset, self.width * 3.25, self.height + 10)
        return QRectF(self.x - offset, self.y - offset, self.width * 5 + 5, self.height)

    def paint(self, qpainter, qstyle_option_graphics_item, widget=None):
        qpainter.setPen(Qt.NoPen)
        qpainter.drawRect(self.x, self.y, self.width, self.height)

        current_index_state = np.where(self.state == 1)[0][0]
        # print(f"RectButton[{self.id}]Being Painted...")
        # print("current index is, ", current_index_state)

        if current_index_state == 0:
            self.current_color_1 = Qt.red
            # self.current_color_1 = Qt.gray
        else:
            self.current_color_1 = Qt.gray
        if current_index_state == 1:
            self.current_color_2 = Qt.red
        else:
            self.current_color_2 = Qt.gray

        # first rectangle, name of simulation
        qpainter.setBrush(self.current_color)
        qpainter.drawRect(self.x, self.y, self.width, self.height)

        # 2nd rectangle, type of simulation
        new_pos = self.x + self.width + 1
        # second rectangle
        qpainter.setBrush(self.current_color_1)
        qpainter.drawRect(new_pos, self.y, self.width, self.height)

        new_pos_2 = self.x + 2 * self.width + 2
        # third rectangle
        qpainter.setBrush(self.current_color_2)
        qpainter.drawRect(new_pos_2, self.y, self.width, self.height)

        new_pos_3 = self.x + 3 * self.width + 3
        # fourth rectangle
        qpainter.setBrush(self.current_color_2)
        qpainter.drawRect(new_pos_3, self.y, self.width, self.height)

        new_pos_4 = self.x + 4 * self.width + 4
        # fourth rectangle
        qpainter.setBrush(self.current_color_2)
        qpainter.drawRect(new_pos_4, self.y, self.width, self.height)

        # boundingRect
        # qpainter.setPen(Qt.cyan)
        # qpainter.setBrush(Qt.NoBrush)
        # qpainter.drawRect(self.boundingRect())

        # Print SIMU NAME
        qrect = QRectF(self.x, self.y, self.width, self.height)
        qpainter.setPen(Qt.white)
        qpainter.setFont(QFont("Times", 20))
        qpainter.drawText(qrect, Qt.AlignCenter, self.text)

        # Print SIMU TYPE
        qrect = QRectF(new_pos_2, self.y, self.width, self.height)
        qpainter.setPen(Qt.white)
        qpainter.setFont(QFont("Times", 20))
        qpainter.drawText(qrect, Qt.AlignCenter, "Antares Study")

        # Print SIMU STATE SENT
        qrect = QRectF(new_pos_3, self.y, self.width, self.height)
        qpainter.setPen(Qt.white)
        qpainter.setFont(QFont("Times", 20))
        qpainter.drawText(qrect, Qt.AlignCenter, "SENT")

        # Print SIMU STATE SENT
        qrect = QRectF(new_pos_4, self.y, self.width, self.height)
        qpainter.setPen(Qt.white)
        qpainter.setFont(QFont("Times", 20))
        qpainter.drawText(qrect, Qt.AlignCenter, "SENT")

class SimulationTab(QGraphicsItem):
    """
    Simulation tab is a graphical rectangular component, that display the name, type and state of a simulation
    """

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
        super(SimulationTab, self).__init__(self.x, self.y, self.width, self.height)

        # simple state array, represented as a numpy array, 0 = False, 1 = True
        # [0] = ZIPPED, [1] = SENT, [2] = SUBMITTED, [3] = FINISHED, [4] = DELIVERED
        self.state = np.zeros(5)
        print("[0] = ZIPPED, [1] = SENT, [2] = SUBMITTED, [3] = FINISHED, [4] = DELIVERED")
        print("state = ", self.state)

        self.mpen = scene_objects.initialize_qpen(Qt.gray)

    def boundingRect(self):
        pass

    def paint(self, qpainter, qstyle_option_graphics_item, widget=None):
        qpainter.setPen(self.mpen)
        qpainter.drawRect(self.x, self.y, self.width, self.height)


class SelectFolderButton(QGraphicsRectItem, QObject):
    ID = 0
    speak = Signal(list)

    def __init__(self, x, y, width, height, text):
        """
        A Rectangle with some text in it
        :param text: str
        :param x: float
        :param y: float
        :param height: float
        :param width: float
        """
        self.id = SelectFolderButton.ID
        SelectFolderButton.ID += 1
        print("my self.id = ", str(self.id))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        # super(SelectFolderButton, self).__init__(self.x, self.y, self.width, self.height)
        QObject.__init__(self)
        QGraphicsRectItem.__init__(self, self.x, self.y, self.width, self.height)

        # self.text = HText("Select Folder", self.x + self.width - 20, self.y + height / 2, self, 45)
        # self.text = HText("Select Folder", self.x + 5, self.y + 5, self, 45)

        # simple state array, represented as a numpy array, 0 = False, 1 = True
        # [0] = ZIPPED, [1] = SENT, [2] = SUBMITTED, [3] = FINISHED, [4] = DELIVERED
        self.state = np.zeros(5)
        self.state[0] = 1
        print(self.state.any())
        # indexes = np.array(np.where(self.state == 1))
        # indexes = list(np.where(self.state == 1))
        indexes = np.where(self.state == 1)
        print("TYPE")
        print(type(indexes))
        # indexes.append(3)
        print("index state = ", indexes)
        print("len = ", len(indexes))

        print("state = \n", self.state)

        self.mpen = scene_objects.initialize_qpen(Qt.gray, width=2)
        self.current_color = Qt.darkRed
        self.current_color_1 = Qt.gray
        self.current_color_2 = Qt.gray
        self.i = 0
        print("################################################################################\n")
        self.qfile_name = QFileDialog()

    def mousePressEvent(self, q_mouse_event):
        # parent = self.parentItem()
        # parent.mousePressEvent(q_mouse_event)

        if self.id == 0:
            dir_path_name = self.qfile_name.getExistingDirectory()
            # print("get existing directory : ", QFileDialog().getExistingDirectory())
            # qfile_name = QFileDialog().getOpenFileName()
            print("You choose the file directory: ", dir_path_name)

            simus = []
            # save all directories, ie, Antares simulation
            for elem in os.listdir(dir_path_name):
                if os.path.isdir(os.path.join(dir_path_name, elem)):
                    simus.append(elem)

            print("List of all Simulations: ", simus)
            if simus:
                self.speak.emit(simus)

            self.id += 1

        self.i = (self.i + 1) % 2
        print("self.i = ", self.i)

        self.state = np.zeros(5)
        self.state[self.i] = 1

        self.update()

        # print("you pressed on RectButton with name = " + str(self.text))
        # # print("this item has " + str(len(self.parents)) + " parents")
        # if self.parent:
        #     print(self.parent)
        #     if isinstance(self.parent, Signal):
        #         self.parent.mousePressEvent(q_mouse_event)
        #     else:
        #         self.parent.mousePressEvent(q_mouse_event)

    def boundingRect(self):
        offset = 0.5
        # return QRectF(self.x - offset, self.y - offset, self.width * 3.25, self.height + 10)
        return QRectF(self.x - offset, self.y - offset, self.width + 4, self.height)

    def paint(self, qpainter, qstyle_option_graphics_item, widget=None):
        qpainter.setPen(Qt.NoPen)
        qpainter.drawRect(self.x, self.y, self.width, self.height)

        current_index_state = np.where(self.state == 1)[0][0]
        # print(f"RectButton[{self.id}]Being Painted...")
        # print("current index is, ", current_index_state)

        if current_index_state == 0:
            self.current_color_1 = Qt.red
            # self.current_color_1 = Qt.gray
        else:
            self.current_color_1 = Qt.gray
        if current_index_state == 1:
            self.current_color_2 = Qt.red
        else:
            self.current_color_2 = Qt.gray

        # first rectangle, name of simulation
        qpainter.setBrush(self.current_color)
        qpainter.drawRect(self.x, self.y, self.width, self.height)

        qpainter.setPen(self.mpen)
        # surrounding design
        qrect_surround = QRectF(self.x - 2, self.y - 2, self.width + 4, self.height + 4)
        qpainter.drawRect(qrect_surround)

        # Print Label
        qrect = QRectF(self.x, self.y, self.width, self.height)
        qpainter.setPen(Qt.white)
        qpainter.setFont(QFont("Times", 40))
        qpainter.drawText(qrect, Qt.AlignCenter, self.text)

        # boundingRect
        qpainter.setPen(Qt.cyan)
        qpainter.setBrush(Qt.NoBrush)
        qpainter.drawRect(self.boundingRect())
