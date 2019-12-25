import sys

from PySide2.QtWidgets import QApplication

from metarch.qt_gui.windows import MainWindow


def run():
    print("Kata1 running...")

    app = QApplication()

    main_window = MainWindow()

    # position_x_top_left_window = 1000
    # position_y_top_left_window = 100

    main_window.setGeometry(500, 100, 1500, 1200)
    # main_window.setGeometry(500, 100, 100, 100)
    main_window.show()

    sys.exit(app.exec_())
