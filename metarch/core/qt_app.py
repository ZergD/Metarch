from PySide2.QtQuick import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pathlib import Path

# from PySide2.QtQml import *

CWD = Path.cwd()

class MyView(QGraphicsView, QObject):
    spaceBar_Bool = False
    # changedZoomValue = QtCore. pyqtSignal(float, name='changedZoomValue')
    viewID = 0

    def __init__(self, scene):
        super(MyView, self).__init__(scene)
        self.myViewID = MyView.viewID
        MyView.viewID = MyView.viewID + 1
        self.zoomFactor = 1
        self.scale(0.8, 0.8)
        self.scale(0.8, 0.8)

        self.numScheduledScalings = 0.0
        self.anim = None
        self.zoom = 1
        self.rotate = 0

        self.setInteractive(True)
        self.setCacheMode(QGraphicsView.CacheBackground)

        self.centerOn(QPoint(10, 500))

        self.selectedItems = None


class Block(QGraphicsRectItem):
    ID = 0

    def __init__(self, ID, name, x, y, width):
        self.ID = int(ID)
        self.x = x
        self.y = y
        self.width = width
        self.height = 20

        super(Block, self).__init__(x, y, width, 20)
        print(f"Block n°{Block.ID} has been printed")


class MyScene(QGraphicsScene):
    ID = 0

    def __init__(self):
        super(MyScene, self).__init__()

        print("Scene representing Line MOVABLE POINT TEST got created")
        self.setBackgroundBrush(Qt.black)
        self.setSceneRect(-1000, 0, 15000, 2500)
        self.setSceneRect(-1000, 0, 15000, 2500)
        self.setSceneRect(0, 0, 1200, 800)

        self.addItem(Block(10, "B1", 10, 500, 50))

        # self.rubberBand = QRubberBand(QRubberBand.Rectangle)
        # self.origin = None


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.scene = MyScene()
        # self.view = QGraphicsView(self.scene)
        self.view = MyView(self.scene)
        self.view = QQuickView()
        self.view.setResizeMode(QQuickView.SizeRootObjectToView)
        qml_file_path = CWD / "app2.qml"
        self.view.setSource(QUrl.fromLocalFile(str(qml_file_path)))
        # self.view.root

        self.setWindowTitle("Antares Study Launcher")


        self.setCentralWidget(self.view)


def run_old(sys):
    print(qVersion())

    # app = QCoreApplication(sys.argv)
    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_window.setGeometry(1000, 100, 1200, 800)
    # main_window.showMaximized()

    main_window.show()

    return app.exec_()


# run with engine
def run(sys):
    print(qVersion())
    app = QGuiApplication(sys.argv)




def run_old2(sys):
    print(qVersion())

    # Setup App window
    app = QGuiApplication(sys.argv)



    # engine = QQmlApplicationEngine("app.qml")
    # context = engine.rootContext()
    # engine.load("app.qml")

    view = QQuickView()

    colors = ["red", "green", "blue"]

    context = view.rootContext()
    context.setContextProperty("colorModel", colors)

    view.setResizeMode(QQuickView.SizeRootObjectToView)

    # load qml file
    qml_file = str(Path.cwd() / "app2.qml")
    view.setSource(QUrl.fromLocalFile(qml_file))

    # Show the window
    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()

    # Execute and cleanup
    app.exec_()
