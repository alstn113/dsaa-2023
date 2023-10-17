class InputView:
    def __init__(self):
        pass

    def read_mathematical_expression(self):
        """
        수식을 입력받는다. 
        빈 문자열이면 에러를 던진다.
        """
        expression = input("입력 수식: ")
        print()
        if (expression == ""):
            raise Exception("Empty expression provided.")
        return expression
