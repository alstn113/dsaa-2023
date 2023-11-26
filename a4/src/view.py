import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QFileDialog
from controller import TreeController

class MainView(QWidget):
    def __init__(self, tree_controller: "TreeController"):
        super().__init__()

        self.file_sort_controller = tree_controller
        self.init_ui()

    def init_ui(self):
        pass