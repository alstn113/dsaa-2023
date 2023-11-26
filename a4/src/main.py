import sys
from PyQt5.QtWidgets import QApplication
from view import MainView


def main():
    """
    프로그램 시작점
    """
    app = QApplication(sys.argv)

    main_view = MainView()

    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
