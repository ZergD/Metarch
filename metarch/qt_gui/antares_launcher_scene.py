import os
from pathlib import Path

from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QColor, QGradient, QLinearGradient
from PySide2.QtWidgets import QGraphicsScene

from metarch.qt_gui import scene_objects
from metarch.qt_gui.scene_objects.rect_buttons import RectButton, SelectFolderButton, LaunchButton, CurrentFolderDisplay


class AntaresLauncherScene(QGraphicsScene):
    """
    Size of the scene has to be: [1440, 810], ie,  x = -720, y, -405, width = 1440, height = 810
    """

    def __init__(self):
        super(AntaresLauncherScene, self).__init__()

        # ################## DATA PART ##################
        self.simulations = []

        # ################## INIT SCENE ##################
        # self.setBackgroundBrush(Qt.black)

        qgradient = QLinearGradient()
        qgradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        # qgradient.setColorAt(0.2, QColor("#180d28"))
        # qgradient.setColorAt(1.0, QColor("#001029"))
        qgradient.setColorAt(0.2, QColor("#001029"))
        qgradient.setColorAt(1.0, QColor("#180d28"))

        # self.setBackgroundBrush(QColor(17, 36, 71))
        # self.setBackgroundBrush(QColor("#180d28"))
        self.setBackgroundBrush(qgradient)
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

        # axis = scene_objects.init_visual_scene_axis()
        # for ax in axis:
        #     self.addItem(ax)
        #     print(f"object {ax} has been added to the scene")

        # ####################################################
        simulations = ["BP_2019", "BP_2020", "BP_2021"]
        positions = [(-400, 100), (-400, 300), (-400, -100)]

        # select_folder = SelectFolderButton(0, 0, 300, 75, "Select Folder")
        # select_folder = SelectFolderButton(608, 50, 300, 75, "Select Folder")
        select_folder = SelectFolderButton(1150, 55, 300, 75, "Select Folder")
        self.addItem(select_folder)
        launch_button = LaunchButton(1150, 355, 300, 75, "Launch...")
        self.addItem(launch_button)

        # Text display for currentFolderDisplay

        # str representing the current_dir
        self.current_dir = None
        self.current_dir_display = CurrentFolderDisplay(50, 60, 750, 40,
                                                        f" Simulations loaded from folder : {self.current_dir}")
        self.addItem(self.current_dir_display)
        select_folder.speak.connect(self.current_dir_display.on_update)

        select_folder.speak.connect(self.init_all_simus_blocks)
        # ################ PART TO AUTO LOAD SIMUS ################
        # self.auto_load_simus_blocks()

    def auto_load_simus_blocks(self):
        simus = []
        dir_path_name = str(Path("E:/Users/Zerg/Documents"))

        for elem in os.listdir(dir_path_name):
            if os.path.isdir(os.path.join(dir_path_name, elem)):
                simus.append(elem)

        self.init_all_simus_blocks(["data", simus])

    @Slot(list)
    def init_all_simus_blocks(self, data):
        # data[0] = selected_folder_str, data[1] = simus
        simus = data[1]
        y_offset = 50
        y = 100
        for i, simu in enumerate(simus, 1):
            x = 50
            y += 60
            # first proposition
            # width = 200
            # height = 50

            # smaller proposition
            # width = 350
            # height = 30

            width = 200
            height = 30
            sim = RectButton(x, y, width, height, simu)
            self.addItem(sim)

        # self.setSceneRect(0.0, 0.0, 1440, 810 + len(simus) * 100)
        # self.setSceneRect(self.x, self.y, self.width, self.height + len(simus) * 100)

    # def mousePressEvent(self, event):
    #     if event.buttons() == Qt.LeftButton:
    #         print(f"You clicked on position [{event.scenePos().x()}, {event.scenePos().y()}]")
