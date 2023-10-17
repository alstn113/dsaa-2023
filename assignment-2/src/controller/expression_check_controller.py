from view.input_view import InputView
from view.output_view import OutputView
from service.expression_check_service import ExpressionCheckService


class ExpressionCheckController:
    def __init__(self, input_view: InputView, output_view: OutputView, expression_check_service: ExpressionCheckService):
        self.input_view = input_view
        self.output_view = output_view
        self.expression_check_service = expression_check_service

    def read_mathematical_expression(self):
        """
        수식을 입력받는다.
        에러가 있으면 에러를 출력하고 끝낸다.
        """
        try:
            expression = self.input_view.read_mathematical_expression()
            return expression
        except Exception as e:
            self.output_view.print_error(e)
            raise e

    def validate_expression(self, expression) -> bool:
        """
        수식의 유효성을 검사한다.
        """
        is_valid, history = self.expression_check_service.validate_expression_with_history(
            expression)
        self.output_view.print_history(history)
        return is_valid

    def print_result(self, is_valid: bool):
        """
        수식의 유효성 검사 결과를 출력한다.
        """
        if is_valid:
            self.output_view.print("Valid expression.")
        else:
            self.output_view.print("Invalid expression.")
