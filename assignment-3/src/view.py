import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QFileDialog
from controller import FileSortController

class MainView(QWidget):
    def __init__(self, file_sort_controller: "FileSortController"):
        super().__init__()

        self.file_sort_controller = file_sort_controller
        self.file_list = []

        self.selected_folder_label = QLabel("Selected Folder: ")
        self.select_folder_button = QPushButton("Select Folder")
        self.sort_algorithm_label = QLabel("Sorting Algorithm: ")
        self.sort_algorithm_combobox = QComboBox()
        self.sort_criteria_label = QLabel("Sorting Criteria: ")
        self.sort_criteria_combobox = QComboBox()
        self.sort_order_label = QLabel("Sorting Order: ")
        self.sort_order_combobox = QComboBox()
        self.elapsed_time_label = QLabel("Elapsed Time: ")
        self.start_sorting_button = QPushButton("Start Sorting")
        self.sort_algorithm_combobox.addItems(["Bubble Sort", "Selection Sort", "Selection Sort", "Quick Sort", "Merge Sort"])
        self.sort_criteria_combobox.addItems(["File Name", "Creation Date", "File Size"])
        self.sort_order_combobox.addItems(["Ascending", "Descending"])

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        folder_layout = QHBoxLayout()
        folder_layout.addWidget(self.selected_folder_label)
        folder_layout.addWidget(self.select_folder_button)

        algorithm_layout = QHBoxLayout()
        algorithm_layout.addWidget(self.sort_algorithm_label)
        algorithm_layout.addWidget(self.sort_algorithm_combobox)

        criteria_layout = QHBoxLayout()
        criteria_layout.addWidget(self.sort_criteria_label)
        criteria_layout.addWidget(self.sort_criteria_combobox)
        criteria_layout.addWidget(self.sort_order_label)
        criteria_layout.addWidget(self.sort_order_combobox)

        time_layout = QHBoxLayout()
        time_layout.addWidget(self.elapsed_time_label)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_sorting_button)

        layout.addLayout(folder_layout)
        layout.addLayout(algorithm_layout)
        layout.addLayout(criteria_layout)
        layout.addLayout(time_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.setWindowTitle('File Sort Manager')
        self.setGeometry(300, 300, 400, 200)

        self.select_folder_button.clicked.connect(self.show_folder_dialog)
        self.start_sorting_button.clicked.connect(self.start_sorting)

    def show_folder_dialog(self):
        folder_dialog = QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(self, "Select Folder")

        if not folder_path:
            return

        folder_name = os.path.basename(folder_path)
        self.selected_folder_label.setText(f"Selected Folder: {folder_name}")

        file_list = []
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if not os.path.isfile(file_path):
                continue

            # File Name, Creation Date, File Size
            file_info = {
                "File Name": file_name,
                "Creation Date": os.path.getctime(file_path),
                "File Size": os.path.getsize(file_path)
            }
            file_list.append(file_info)

        self.file_list = file_list

    def start_sorting(self):
        sorted_data, history, elapsed_time = self.file_sort_controller.sort_data(
            self.file_list,
            self.sort_algorithm_combobox.currentText(),
            self.sort_criteria_combobox.currentText(),
            self.sort_order_combobox.currentText(),
        )

        print(sorted_data)
        print(history)
        
        self.elapsed_time_label.setText(f"Elapsed Time: {elapsed_time * 1000:.2f} ms")