import os
import random
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QFileDialog
from controller import FileSortController

sort_time_complexity = {
    "Bubble Sort": "O(n^2)",
    "Selection Sort": "O(n^2)",
    "Insertion Sort": "O(n^2)",
    "Quick Sort": "O(nlogn)",
    "Merge Sort": "O(nlogn)"
}

class MainView(QWidget):
    def __init__(self, file_sort_controller: "FileSortController"):
        super().__init__()

        self.file_sort_controller = file_sort_controller
        self.file_list = []

        self.selected_folder_label = QLabel("선택된 폴더: ")
        self.select_folder_button = QPushButton("폴더 선택")
        self.sort_algorithm_label = QLabel("정렬 알고리즘: ")
        self.sort_algorithm_combobox = QComboBox()
        self.sort_criteria_label = QLabel("정렬 기준: ")
        self.sort_criteria_combobox = QComboBox()
        self.sort_order_label = QLabel("정렬 순서: ")
        self.sort_order_combobox = QComboBox()
        self.elapsed_time_label = QLabel("걸린 시간: ")
        self.start_sorting_button = QPushButton("정렬 시작")
        self.sort_algorithm_combobox.addItems(["Bubble Sort", "Selection Sort", "Insertion Sort", "Quick Sort", "Merge Sort"])
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
        algorithm = self.sort_algorithm_combobox.currentText()
        criteria = self.sort_criteria_combobox.currentText()
        order = self.sort_order_combobox.currentText()

        # 선택된 파일이 없을 경우 랜덤 파일을 생성한다.
        if self.file_list == []:
            self.__generate_random_files()

        sorted_data, history, elapsed_time = self.file_sort_controller.sort_data(
            self.file_list,
            algorithm, 
            criteria,
            order
        )

        for i in range(len(history)):
            print(list(map(lambda x: x[criteria], history[i])))
        print()
        print(f"정렬결과: {sorted_data}")
        
        self.elapsed_time_label.setText(f"걸린 시간: {elapsed_time * 1000:.2f} ms / 시간 복잡도: {sort_time_complexity[algorithm]}")

    def __generate_random_files(self):
        # 현재 위치에 폴더를 생성한다.
        # 폴더 이름은 랜덤한 문자열로 생성한다.

        folder_name = "random_files_" + str(random.randint(1, 1000))
        folder_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(folder_path, exist_ok=True)

        self.selected_folder_label.setText(f"Selected Folder: {folder_name}")

        # 랜덤 파일을 여러개 생성한다.
        for _ in range(100):
            random_file_name = ''.join(random.choice('0123456789ABCDEF') for i in range(4)) + ".txt"
            random_file_path = os.path.join(folder_path, random_file_name)
            with open(random_file_path, 'w') as file:
                file.write("Random file content")

        file_list = []
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                file_info = {
                    "File Name": file_name,
                    "Creation Date": os.path.getctime(file_path),
                    "File Size": os.path.getsize(file_path)
                }
                file_list.append(file_info)

        self.file_list = file_list