from PySide2.QtCore import Qt, QPoint
from PySide2.QtWidgets import QGraphicsScene

from metarch.qt_gui import scene_objects
from metarch.qt_gui.scene_objects.circles import Circle


class AntaresLauncherScene(QGraphicsScene):

    def __init__(self):
        super(AntaresLauncherScene, self).__init__()

        # ################## INIT SCENE ##################
        self.setBackgroundBrush(Qt.black)
        # self.setSceneRect(-1000, -1000, 2000, 2000)
        self.setSceneRect(-500, -500, 1000, 1000)

        # self.addItem(Circle(QPoint(10, 10)))

        axis = scene_objects.init_visual_scene_axis()
        for ax in axis:
            self.addItem(ax)
            print(f"object {ax} has been added to the scene")

        # ####################################################
        simulations = ["BP_2019", "BP_2020", "BP_2021"]
        positions = []

        # for simulation in simulations:
        #     self.addItem()

        for simulation in simulations:
            print(f"added simulation: {simulation}")






