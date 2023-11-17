import sys
from PyQt5.QtWidgets import QApplication
from controllers.image_slide_controller import ImageSlideController
from views.main_view import MainView


def main():
    """
    프로그램 시작점
    """
    app = QApplication(sys.argv)

    image_slide_controller = ImageSlideController()
    main_view = MainView(
        image_slide_controller,
    )

    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
