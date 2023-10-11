import unittest
from service.expression_check_service import ExpressionCheckService


class ExpressionCheckTest(unittest.TestCase):
    def setUp(self):
        self.expression_check_service = ExpressionCheckService()

    def test_expression_validation(self):
        test_list = [
            (False, "([[])"),
            (True, "[{(3+2) - [4/(2*1)]} + {2*3}]"),
            (True,
             "[(3 + 5) * {4 - (7 / 2)} - [8 * (2 + 3) - {9 / (3 + 4)}]]"),
            (True, "{sin[(3 + 5) * (7 - 4)] + cos[2 * π * (3 + 2)]} / {1 + tan[π/4]}"),
            (True, "[{(3 + 5) > (4 - 2)} && {(8 / 2) <= (5 * 2)}] || [{3 * (2 + 1)} == 9]"),
            (True,
             "arr[[(i + 1) * 3] - {j - 1}] = matrix[2][3 + {k/(2 + 1)}]"),
            (False, "f(g[{h(3 + 5) * 2} - {i(1/2)}], j[k(3 + {l(4 * m(5))}])"),
            (False, "(3 + 5 _ {4 - 2)"),
            (False, "3 + 5) _ {4 - 2}"),
            (False, "[(3 + 5) * {4 - 2)]"),
            (False, "(3 + 5) _ (4 - 2))"),
            (False, "[3 + 5 _ {4 - 2}}]"),
            (True, "{(3 + 5) _ [4 - 2]}"),
            (False, "[3 + 5 _ {4 - 2] - 3}"),

        ]

        for expected_result, expression in test_list:
            is_valid = self.expression_check_service.checkIsValidExpressionWithHistory(
                expression)[0]
            self.assertEqual(is_valid, expected_result)


if __name__ == "__main__":
    unittest.main()
