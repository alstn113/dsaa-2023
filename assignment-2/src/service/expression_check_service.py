from domain.Stack import Stack


class ExpressionCheckService:
    def __init__(self):
        self.bracket_pairs = {')': '(', ']': '[', '}': '{'}
        self.opening_brackets = [*self.bracket_pairs.values()]
        self.closing_brackets = [*self.bracket_pairs.keys()]

    def validate_expression_with_history(self, expression: str) -> bool:
        """
        수식이 유효한지 검사합니다.
        :param expression: 수식
        :return: 유효 여부, stack 변화 과정
        """
        stack = Stack()
        is_valid = True
        history = []

        for char in expression:
            if char in self.opening_brackets:
                stack.push(char)
            elif char in self.closing_brackets:
                is_valid = self._check_closing_bracket(stack, char)
            else:
                continue

            history.append(f"입력값: {char}")
            # 스택 변화 과정을 기록합니다.
            history.append(str(stack) + "\n")  # stack.__repr__() 호출

            # 유효하지 않은 수식이라면 검사를 종료합니다.
            if not is_valid:
                break

        # 마지막에 스택에 남아있는 여는 괄호가 있다면 유효하지 않은 수식입니다.
        return is_valid and stack.is_empty(), history

    def _check_closing_bracket(self, stack: "Stack", char: str) -> bool:
        """
        닫는 괄호가 유효한지 검사합니다.
        """
        # 스택이 비어있거나, 짝이 맞지 않는다면 유효하지 않은 수식입니다.
        if stack.is_empty() or stack.peek().data != self.bracket_pairs[char]:
            return False

        # 짝이 맞는다면 스택에서 꺼냅니다.
        stack.pop()
        return True
