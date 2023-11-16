import sys
from PyQt5.QtWidgets import QApplication
from controller import FileSortController
from service import FileSortService
from view import MainView


def main():
    """
    프로그램 시작점
    """
    app = QApplication(sys.argv)

    image_slide_controller = FileSortController(
        FileSortService()
    )
    main_view = MainView(
        image_slide_controller,
    )

    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
