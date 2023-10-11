from controller.expression_check_controller import ExpressionCheckController
from view.input_view import InputView
from view.output_view import OutputView
from service.expression_check_service import ExpressionCheckService


def main():
    expression_controller = ExpressionCheckController(
        InputView(),
        OutputView(),
        ExpressionCheckService()
    )

    try:
        expression = expression_controller.readMathematicalExpression()
        is_valid = expression_controller.checkIsValidExpression(expression)
        expression_controller.printResult(is_valid)
    except Exception:
        return


if __name__ == "__main__":
    main()
