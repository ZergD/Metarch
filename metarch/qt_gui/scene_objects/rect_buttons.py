import numpy as np
from PySide2.QtCore import Qt, QRectF, Signal, QObject
from PySide2.QtGui import QFont, QColor
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
        self.font_size = 10

        # this is the width of all the fields, ZIPPED, SENT, SUBMITTED, FINISHED, HOME
        self.width_field = self.width / 2
        super(RectButton, self).__init__(self.x, self.y, self.width * 5, self.height)

        # simple state array, represented as a numpy array, 0 = False, 1 = True
        # [0] = ZIPPED, [1] = SENT, [2] = SUBMITTED, [3] = FINISHED, [4] = DELIVERED
        self.state = np.zeros(5)
        self.state[0] = 1
        # print(self.state.any())
        # indexes = np.array(np.where(self.state == 1))
        # indexes = list(np.where(self.state == 1))
        indexes = np.where(self.state == 1)

        # print("state = \n", self.state)

        self.mpen = scene_objects.initialize_qpen(Qt.black, width=1)
        # self.main_background_color = QColor("43, 43, 43")
        # self.main_background_color = QColor("60, 63, 65")
        self.main_background_color = Qt.gray
        # self.current_color = Qt.gray
        self.current_color = self.main_background_color

        # ZIPPED SENT SUBMITTED FINISHED HOME
        self.states_colors = []
        self.nb_states = 5
        for i in range(self.nb_states):
            # self.states_colors.append(Qt.gray)
            self.states_colors.append(self.current_color)

        self.i = 0
        # print("################################################################################\n")
        self.qfile_name = QFileDialog()
        self.setAcceptHoverEvents(True)
        self.show_border_flag = False

    def hoverEnterEvent(self, event):
        # print("In Enter Event")
        # self.mpen.setColor(Qt.gray)
        self.show_border_flag = True
        self.update()

    def hoverLeaveEvent(self, event):
        # print("Out Enter Event")
        # self.mpen.setColor(Qt.black)
        self.show_border_flag = False
        self.update()

    def mousePressEvent(self, q_mouse_event):
        # parent = self.parentItem()
        # parent.mousePressEvent(q_mouse_event)

        self.i = (self.i + 1) % 5

        if self.state.all():
            # print("Full 1 vector")
            self.state = np.zeros(5)
            self.i = 0

        # if self.id == 0:
        #     # print("we create a QFileDialog")
        #     # qfile_name = QFileDialog().getOpenFileName("Choose a Simulation Folder", str(Path.cwd()))
        #     qfile_name = self.qfile_name.getExistingDirectory()
        #     # print("get existing directory : ", QFileDialog().getExistingDirectory())
        #     # qfile_name = QFileDialog().getOpenFileName()
        #     print("You choose the file directory: ", qfile_name)
        #     self.id += 1

        # print("after iterating: self.i = ", self.i)

        self.state = np.zeros(5)
        # self.state[self.i] = 1

        for i in range(0, self.i + 1):
            self.state[i] = 1

        # print(self.state)

        # current_index_state = np.where(self.state == 1)[0]

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
        # offset = 0.5
        offset = 1
        # return QRectF(self.x - offset, self.y - offset, self.width * 3.25, self.height + 10)
        return QRectF(self.x - offset, self.y - offset, self.width * 5 + 5, self.height)

    def paint(self, qpainter, qstyle_option_graphics_item, widget=None):
        if self.show_border_flag:
            self.mpen.setColor(Qt.black)
            self.mpen.setWidth(1)
            qpainter.setPen(self.mpen)
            # qpainter.setPen(Qt.black)
        else:
            qpainter.setPen(Qt.NoPen)

        current_index_state = np.where(self.state == 1)[0]
        # print(f"RectButton[{self.id}]Being Painted...")
        # print("current index is, ", current_index_state)

        # first rectangle, name of simulation
        qpainter.setBrush(self.current_color)
        qpainter.drawRect(self.x, self.y, self.width, self.height)

        # second rectangle, type of simulation
        pos_type_text = self.x + self.width + 2
        qpainter.setBrush(self.current_color)
        qpainter.drawRect(pos_type_text, self.y, self.width, self.height)

        # Print SIMU NAME
        qrect = QRectF(self.x, self.y, self.width, self.height)
        qpainter.setPen(Qt.white)
        qpainter.setFont(QFont("Times", self.font_size))
        qpainter.drawText(qrect, Qt.AlignCenter, self.text)

        # Print SIMU TYPE
        qrect = QRectF(pos_type_text, self.y, self.width, self.height)
        qpainter.setPen(Qt.white)
        qpainter.setFont(QFont("Times", self.font_size))
        qpainter.drawText(qrect, Qt.AlignCenter, "Antares Study")

        for i in range(len(self.state)):
            if i in current_index_state:
                self.states_colors[i] = Qt.red
            else:
                self.states_colors[i] = Qt.gray

        # print("states_colors = ", self.states_colors)
        # print(self.state)

        for i, color in enumerate(self.states_colors, 0):
            new_pos = self.x + 2 * self.width + i * self.width_field + (2 * i)
            qrect = QRectF(new_pos, self.y, self.width_field, self.height)

            # print(f"for i = {str(i)} color = {color}")
            qpainter.setBrush(color)
            qpainter.setPen(Qt.NoPen)
            qpainter.drawRect(qrect)

            qpainter.setPen(Qt.white)
            qpainter.setFont(QFont("Times", self.font_size))

            if i == 0:
                qpainter.drawText(qrect, Qt.AlignCenter, "ZIPPED")
            elif i == 1:
                qpainter.drawText(qrect, Qt.AlignCenter, "SENT")
            elif i == 2:
                qpainter.drawText(qrect, Qt.AlignCenter, "SUBMITTED")
            elif i == 3:
                qpainter.drawText(qrect, Qt.AlignCenter, "FINISHED")
            elif i == 4:
                qpainter.drawText(qrect, Qt.AlignCenter, "HOME")

        # boundingRect
        if self.show_border_flag:
            self.mpen.setColor(Qt.white)
            self.mpen.setWidth(1)
            qpainter.setPen(self.mpen)
            qpainter.setBrush(Qt.NoBrush)
            offset = 0.6
            qrect = QRectF(self.x - offset, self.y - offset, self.width * 2 + self.width_field * 5 + 10, self.height)
            qpainter.drawRect(qrect)


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
        # qpainter.setPen(Qt.cyan)
        # qpainter.setBrush(Qt.NoBrush)
        # qpainter.drawRect(self.boundingRect())


class LaunchButton(QGraphicsRectItem, QObject):
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
        self.id = LaunchButton.ID
        LaunchButton.ID += 1
        print("my self.id = ", str(self.id))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        # super(SelectFolderButton, self).__init__(self.x, self.y, self.width, self.height)
        QObject.__init__(self)
        QGraphicsRectItem.__init__(self, self.x, self.y, self.width, self.height)
        self.setAcceptHoverEvents(True)

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

        self.mpen = scene_objects.initialize_qpen(QColor(7, 133, 192), width=2)

        # main block color
        self.current_color = QColor(7, 133, 192)

        # self.current_color_1 = Qt.gray
        # self.current_color_2 = Qt.gray
        self.i = 0
        print("################################################################################\n")

    def mousePressEvent(self, q_mouse_event):
        # parent = self.parentItem()
        # parent.mousePressEvent(q_mouse_event)
        print("Initiating Launch Sequence...")
        print("Starting Launch Sequence...\n")
        self.current_color = QColor(0, 105, 153)
        self.update()

        # if self.id == 0:
        #     dir_path_name = self.qfile_name.getExistingDirectory()
        #     # print("get existing directory : ", QFileDialog().getExistingDirectory())
        #     # qfile_name = QFileDialog().getOpenFileName()
        #     print("You choose the file directory: ", dir_path_name)
        #
        #     simus = []
        #     # save all directories, ie, Antares simulation
        #     for elem in os.listdir(dir_path_name):
        #         if os.path.isdir(os.path.join(dir_path_name, elem)):
        #             simus.append(elem)
        #
        #     print("List of all Simulations: ", simus)
        #     if simus:
        #         self.speak.emit(simus)
        #
        #     self.id += 1
        #
        # self.i = (self.i + 1) % 2
        # print("self.i = ", self.i)
        #
        # self.state = np.zeros(5)
        # self.state[self.i] = 1
        #
        # self.update()

    def mouseReleaseEvent(self, event):
        self.current_color = QColor(7, 133, 192)
        self.update()

    def hoverEnterEvent(self, event):
        print("enter event")
        self.current_color = QColor(38, 180, 245)
        self.update()

    def hoverLeaveEvent(self, event):
        self.current_color = QColor(7, 133, 192)
        self.update()

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

        # if current_index_state == 0:
        #     self.current_color_1 = Qt.red
        #     # self.current_color_1 = Qt.gray
        # else:
        #     self.current_color_1 = Qt.gray
        # if current_index_state == 1:
        #     self.current_color_2 = Qt.red
        # else:
        #     self.current_color_2 = Qt.gray

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
        # qpainter.setPen(Qt.cyan)
        # qpainter.setBrush(Qt.NoBrush)
        # qpainter.drawRect(self.boundingRect())
