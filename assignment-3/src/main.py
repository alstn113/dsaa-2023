import sys
from PyQt5.QtWidgets import QApplication
from controller import FileSortController
from view import MainView


def main():
    """
    프로그램 시작점
    """
    app = QApplication(sys.argv)

    file_sort_controller = FileSortController()
    main_view = MainView(
        file_sort_controller,
    )

    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
