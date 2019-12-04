import os
from pathlib import Path

from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import QGraphicsScene

from metarch.qt_gui import scene_objects
from metarch.qt_gui.scene_objects.rect_buttons import RectButton, SelectFolderButton


class AntaresLauncherScene(QGraphicsScene):
    """
    Size of the scene has to be: [1440, 810], ie,  x = -720, y, -405, width = 1440, height = 810
    """

    def __init__(self):
        super(AntaresLauncherScene, self).__init__()

        # ################## DATA PART ##################
        self.simulations = []

        # ################## INIT SCENE ##################
        self.setBackgroundBrush(Qt.black)
        self.setSceneRect(0, 0, 2000, 2000)
        # self.x = -720
        # self.y = -405
        # self.width = 1440
        # self.height = 810
        # self.setSceneRect(-720, -405, 1440, 810)
        # self.setSceneRect(0, 0, 1440, 810)

        # don't understand why its not exactly 0,0 ton top left corner, if you print scene:mousePressEvent()scene.Pos()
        # if SceneRect.width is < than width of Window, then the scene grows de part et d'autre
        # |win  <-- |scene| --> win |
        # |-5.0  <-- |0, 1400| --> 1405 |
        # self.setSceneRect(0.0, 0.0, 1440, 810)

        # self.addItem(Circle(QPoint(10, 10)))

        axis = scene_objects.init_visual_scene_axis()
        for ax in axis:
            self.addItem(ax)
            print(f"object {ax} has been added to the scene")

        # ####################################################
        simulations = ["BP_2019", "BP_2020", "BP_2021"]
        positions = [(-400, 100), (-400, 300), (-400, -100)]

        # for simulation in simulations:
        #     self.addItem()
        # for simulation, position in zip(simulations, positions):
        #     print(f"added simulation: {simulation} at position: {position}")
        #     sim = RectButton(position[0], position[1] - 400, 50, 200, "Hello")
        #     self.addItem(sim)

        # select_folder = RectButton(0, -525, 300, 75, "Select Folder")
        # select_folder = SelectFolderButton(-160, -525, 300, 75, "Select Folder")

        # select_folder = SelectFolderButton(0, 0, 300, 75, "Select Folder")
        select_folder = SelectFolderButton(608, 50, 300, 75, "Select Folder")
        self.addItem(select_folder)

        # select_folder.speak.connect(self.init_all_simus_blocks)
        simus = []
        dir_path_name = str(Path("E:/Users/Zerg/Documents").expanduser())

        for elem in os.listdir(dir_path_name):
            if os.path.isdir(os.path.join(dir_path_name, elem)):
                simus.append(elem)

        self.init_all_simus_blocks(simus)

    @Slot(list)
    def init_all_simus_blocks(self, simus):
        offset = 100
        for i, simu in enumerate(simus, 1):
            x = 50
            y = i * 100 + offset
            # first proposition
            # width = 200
            # height = 50

            # smaller proposition
            width = 250
            height = 30
            sim = RectButton(x, y, width, height, simu)
            self.addItem(sim)

        # self.setSceneRect(0.0, 0.0, 1440, 810 + len(simus) * 100)
        # self.setSceneRect(self.x, self.y, self.width, self.height + len(simus) * 100)

    # def mousePressEvent(self, event):
    #     if event.buttons() == Qt.LeftButton:
    #         print(f"You clicked on position [{event.scenePos().x()}, {event.scenePos().y()}]")
