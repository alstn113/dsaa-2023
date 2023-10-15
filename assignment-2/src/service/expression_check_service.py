from domain.Stack import Stack


class ExpressionCheckService:
    def __init__(self):
        pass

    def checkIsValidExpressionWithHistory(self, expression) -> bool:
        """
        수식이 유효한지 검사합니다.
        :param expression: 수식
        :return: 유효 여부, stack 변화 과정
        """
        stack = Stack()
        bracket_pairs = {')': '(', ']': '[', '}': '{'}
        is_valid = True
        history = []

        for char in expression:
            if char not in "[](){}":
                continue
            history.append(f"입력값: {char}")

            if char in '([{':
                stack.push(char)
            elif char in ')]}':
                if stack.is_empty() or stack.peek().data != bracket_pairs[char]:
                    is_valid = False
                else:
                    stack.pop()

            history.append(str(stack))
            history.append("")
            if not is_valid:
                break

        return is_valid and stack.is_empty(), history
