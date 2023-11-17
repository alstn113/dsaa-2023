from service.expression_check_service import ExpressionCheckService


class ExpressionCheckController:
    def __init__(self, expression_check_service: ExpressionCheckService):
        self.expression_check_service = expression_check_service

    def validate_expression_with_history(self, expression) -> (bool, list):
        """
        수식의 유효성을 검사한다.
        """
        is_valid, history = self.expression_check_service.validate_expression_with_history(
            expression)

        return is_valid, history
