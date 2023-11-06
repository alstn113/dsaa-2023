import sys
from PyQt5.QtWidgets import QApplication
from controller.file_sort_contorller import FileSortController
from service.file_sort_service import FileSortService
from view.main_view import MainView

def main():
    app = QApplication(sys.argv)

    main_view = MainView(
        FileSortController(
           FileSortService()
        )
    )

    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
