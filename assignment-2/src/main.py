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
        expression = expression_controller.read_mathematical_expression()
        is_valid = expression_controller.validate_expression(expression)
        expression_controller.print_result(is_valid)
    except Exception:
        return


if __name__ == "__main__":
    main()
