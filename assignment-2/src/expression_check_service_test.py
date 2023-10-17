import unittest
from service.expression_check_service import ExpressionCheckService


class ExpressionCheckServiceTest(unittest.TestCase):
    """
    ExpressionCheckService의 테스트 케이스입니다.
    """

    def setUp(self):
        self.expression_check_service = ExpressionCheckService()

    def test_validate_expression_valid_cases(self):
        """
        유효한 수식들을 검사합니다.
        """
        valid_cases = [
            "[{(3+2) - [4/(2*1)]} + {2*3}]",
            "[(3 + 5) * {4 - (7 / 2)} - [8 * (2 + 3) - {9 / (3 + 4)}]]",
            "{sin[(3 + 5) * (7 - 4)] + cos[2 * π * (3 + 2)]} / {1 + tan[π/4]}",
            "[{(3 + 5) > (4 - 2)} && {(8 / 2) <= (5 * 2)}] || [{3 * (2 + 1)} == 9]",
            "arr[[(i + 1) * 3] - {j - 1}] = matrix[2][3 + {k/(2 + 1)}]",
            "{(3 + 5) _ [4 - 2]}",
        ]

        for expression in valid_cases:
            is_valid, _ = self.expression_check_service.validate_expression_with_history(
                expression)
            self.assertTrue(is_valid)

    def test_validate_expression_invalid_cases(self):
        """
        유효하지 않은 수식들을 검사합니다.
        """
        invalid_cases = [
            "([[])",
            "f(g[{h(3 + 5) * 2} - {i(1/2)}], j[k(3 + {l(4 * m(5))}])",
            "(3 + 5 _ {4 - 2)",
            "3 + 5) _ {4 - 2}",
            "[(3 + 5) * {4 - 2)]",
            "(3 + 5) _ (4 - 2))",
            "[3 + 5 _ {4 - 2}}]",
            "[3 + 5 _ {4 - 2] - 3}",
        ]

        for expression in invalid_cases:
            is_valid, _ = self.expression_check_service.validate_expression_with_history(
                expression)
            self.assertFalse(is_valid)


if __name__ == "__main__":
    unittest.main()
