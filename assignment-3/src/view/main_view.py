from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QDesktopWidget, QLineEdit, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

from controller.file_sort_contorller import FileSortController
from view.util import center

class MainView(QMainWindow):
    def __init__(self, file_sort_controller: "FileSortController"):
        super().__init__()
        self.file_sort_controller = file_sort_controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Sort Manager')
        self.resize(450, 350)
        center(self)

        main_layout = QVBoxLayout()

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)



