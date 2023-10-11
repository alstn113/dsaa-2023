import os
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QFileDialog, QDesktopWidget
from PyQt5.QtGui import QPixmap
from controllers.image_slide_controller import ImageSlideController


class MainView(QMainWindow):
    """
    메인 뷰 클래스
    """

    def __init__(self, image_slide_controller: "ImageSlideController"):
        super().__init__()

        self.image_slide_controller = image_slide_controller

        self.initUI()

    def initUI(self):
        """
        UI를 초기화하는 함수
        """
        self.setWindowTitle('Image Slide Show')
        self.resize(450, 350)
        self.center()

        main_layout = QVBoxLayout()

        header_layout = QHBoxLayout()
        image_display_layout = QVBoxLayout()
        footer_layout = QHBoxLayout()

        # 버튼 스타일 설정
        button_style = """
            QPushButton {
                border-radius: 8px; /* 버튼 모서리 둥글게 */
                color: white; /* 텍스트 색상 */
                padding: 10px 20px;
                font-size: 16px;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(128, 128, 128, 255), stop:1 rgba(64, 64, 64, 255));
            }
            QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(128, 128, 128, 150), stop:1 rgba(64, 64, 64, 150));
            }
        """

        add_folder_button = QPushButton("Add Folder")
        add_folder_button.setStyleSheet(button_style)
        add_folder_button.clicked.connect(self.add_folder_button_clicked)

        add_image_button = QPushButton("Add Image")
        add_image_button.setStyleSheet(button_style)
        add_image_button.clicked.connect(self.add_image_button_clicked)

        header_layout.addWidget(add_folder_button)
        header_layout.addWidget(add_image_button)

        self.image_label = QLabel()
        self.image_label.setFixedSize(450, 200)

        image_display_layout.addWidget(self.image_label)

        prev_image_button = QPushButton("Prev Image")
        prev_image_button.setStyleSheet(button_style)
        prev_image_button.clicked.connect(self.prev_image_button_clicked)

        delete_image_button = QPushButton("Delete Image")
        delete_image_button.setStyleSheet(button_style)
        delete_image_button.clicked.connect(self.delete_image_button_clicked)

        next_image_button = QPushButton("Next Image")
        next_image_button.setStyleSheet(button_style)
        next_image_button.clicked.connect(self.next_image_button_clicked)

        footer_layout.addWidget(prev_image_button)
        footer_layout.addWidget(delete_image_button)
        footer_layout.addWidget(next_image_button)

        main_layout.addLayout(header_layout)
        main_layout.addLayout(image_display_layout)
        main_layout.addLayout(footer_layout)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

        self.update_image()

    def center(window):
        """
        창을 화면의 가운데로 이동
        """
        qr = window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        window.move(qr.topLeft())

    def update_image(self):
        """
        현재 이미지를 업데이트하는 함수
        """
        current_image_path = self.image_slide_controller.get_current_image()
        pixmap = QPixmap(current_image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    def prev_image_button_clicked(self):
        """
        이전 이미지 버튼이 클릭되었을 때 호출되는 함수
        """
        self.image_slide_controller.prev_image()
        self.update_image()

    def next_image_button_clicked(self):
        """
        다음 이미지 버튼이 클릭되었을 때 호출되는 함수
        """
        self.image_slide_controller.next_image()
        self.update_image()

    def add_folder_button_clicked(self):
        """
        폴더 추가 버튼이 클릭되었을 때 호출되는 함수
        """
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        folder_path = QFileDialog.getExistingDirectory(
            self, "Select Folder", options=options)

        if folder_path:
            self.image_slide_controller.add_folder(folder_path)
            self.update_image()

    def add_image_button_clicked(self):
        """
        이미지 추가 버튼이 클릭되었을 때 호출되는 함수

        FileDialog가 열리고 이미지를 선택하면 해당 이미지를 src/images 디렉토리로 복사합니다.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog(self)
        file_dialog.setOptions(options)
        file_dialog.setNameFilter(
            'Images (*.png *.jpg *.jpeg );;All Files (*)')

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]
                image_name = os.path.basename(image_path)
                image_createdAt = os.path.getctime(image_path)
                self.image_slide_controller.add_image(
                    image_name, image_path, image_createdAt
                )
                self.update_image()

    def delete_image_button_clicked(self):
        self.image_slide_controller.delete_current()
        self.update_image()
