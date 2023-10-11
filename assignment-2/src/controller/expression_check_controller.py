from view.input_view import InputView
from view.output_view import OutputView
from service.expression_check_service import ExpressionCheckService


class ExpressionCheckController:
    def __init__(self, input_view: InputView, output_view: OutputView, expression_check_service: ExpressionCheckService):
        self.input_view = input_view
        self.output_view = output_view
        self.expression_check_service = expression_check_service

    def readMathematicalExpression(self):
        try:
            expression = self.input_view.readMathematicalExpression()
            return expression
        except Exception as e:
            self.output_view.printError(e)
            raise e

    def checkIsValidExpression(self, expression) -> bool:
        is_valid, history = self.expression_check_service.checkIsValidExpressionWithHistory(
            expression)
        self.output_view.printHistory(history)
        return is_valid

    def printResult(self, is_valid: bool):
        if is_valid:
            self.output_view.print("Valid expression.")
        else:
            self.output_view.print("Invalid expression.")
