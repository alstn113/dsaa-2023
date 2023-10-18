import sys
from PyQt5.QtWidgets import QApplication
from controller.expression_check_controller import ExpressionCheckController
from view.expression_check_view import ExpressionCheckView

from controller.expression_check_controller import ExpressionCheckController
from service.expression_check_service import ExpressionCheckService


def main():
    """
    프로그램 시작점
    """

    app = QApplication(sys.argv)

    expression_check_view = ExpressionCheckView(
        ExpressionCheckController(
            ExpressionCheckService()
        )
    )

    expression_check_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
