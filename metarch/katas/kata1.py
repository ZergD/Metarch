import sys

from PySide2.QtWidgets import QApplication

from metarch.qt_gui.windows import MainWindow


def run():
    print("Kata1 running...")

    app = QApplication()

    main_window = MainWindow()
    main_window.setGeometry(1000, 100, 1500, 1200)
    main_window.show()

    sys.exit(app.exec_())
