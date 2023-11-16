import os
from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QFileDialog
from controller import FileSortController

class MainView(QWidget):
    def __init__(self, file_sort_controller: "FileSortController"):
        super().__init__()

        self.file_sort_controller = file_sort_controller
        self.file_list = []

        self.selected_folder_label = QLabel("선택된 폴더 이름: ")
        self.select_folder_button = QPushButton("폴더 선택")
        self.sort_algorithm_label = QLabel("정렬 알고리즘: ")
        self.sort_algorithm_combobox = QComboBox()
        self.sort_criteria_label = QLabel("정렬 기준: ")
        self.sort_criteria_combobox = QComboBox()
        self.sort_order_label = QLabel("정렬 순서: ")
        self.sort_order_combobox = QComboBox()
        self.elapsed_time_label = QLabel("걸린 시간: ")
        self.start_sorting_button = QPushButton("정렬 시작")
        self.sort_algorithm_combobox.addItems(["버블 정렬", "선택 정렬", "선택 정렬", "퀵 정렬", "병합 정렬"])
        self.sort_criteria_combobox.addItems(["파일 이름", "생성 날짜", "파일 크기"])
        self.sort_order_combobox.addItems(["오름차순", "내림차순"])

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

        self.setWindowTitle('파일 정렬 매니저')
        self.setGeometry(300, 300, 400, 200)

        self.select_folder_button.clicked.connect(self.show_folder_dialog)
        self.start_sorting_button.clicked.connect(self.start_sorting)

    def show_folder_dialog(self):
        folder_dialog = QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(self, "폴더 선택")

        if not folder_path:
            return

        folder_name = os.path.basename(folder_path)
        self.selected_folder_label.setText(f"선택된 폴더 이름: {folder_name}")

        file_list = []
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if not os.path.isfile(file_path):
                continue

            # 파일 이름, 생성 날짜, 파일 크기
            file_info = [file_name, os.path.getctime(file_path), os.path.getsize(file_path)]
            file_list.append(file_info)

        self.file_list = file_list

    def start_sorting(self):

        self.elapsed_time_label.setText(f"걸린 시간: {1.00:.2f} seconds")
        
        print(self.sort_algorithm_combobox.currentText())
        print(self.sort_criteria_combobox.currentText())
        print(self.sort_order_combobox.currentText())
        print(self.file_list)