from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QDesktopWidget, QLineEdit, QWidget, QHBoxLayout
from controller.expression_check_controller import ExpressionCheckController
from PyQt5.QtCore import Qt
from view.utils import center


class ExpressionCheckView(QMainWindow):
    def __init__(self, expression_check_controller: "ExpressionCheckController"):
        super().__init__()
        self.expression_check_controller = expression_check_controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle('괄호 검사기')
        self.resize(450, 150)
        center(self)

        main_layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.input_label = QLabel("입력 수식: ")
        self.input_edit = QLineEdit()
        self.validate_button = QPushButton('검사하기')
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_edit)

        self.validation_result_label = QLabel(
            "결과가 여기에 표시됩니다.")
        self.validation_result_label.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.validate_button)
        main_layout.addWidget(self.validation_result_label)

        self.validate_button.clicked.connect(self.validate_expression)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
            }
            QPushButton {
                font-size: 14px;
                background-color: #4CAF50; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 5px; 
            }
            QPushButton:hover {
                background-color: #45a049; 
            }
        """)

    def validate_expression(self):
        try:
            expression = self.input_edit.text()

            if expression == "":
                raise Exception("Empty expression provided.")

            is_valid, history = self.expression_check_controller.validate_expression_with_history(
                expression)
            result_message = "✅ Valid expression." if is_valid else "❌ Invalid expression."
            self.validation_result_label.setText(result_message)
            self.print_history(history, result_message)
        except Exception as e:
            self.validation_result_label.setText(str(e))
            print(str(e) + "\n")

    def print_history(self, history, result_message):
        for line in history:
            print(line)
        print(result_message)
        print()
