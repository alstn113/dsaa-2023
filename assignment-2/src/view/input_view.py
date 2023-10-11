class InputView:
    def __init__(self):
        pass

    def readMathematicalExpression(self):
        expression = input("입력 수식: ")
        print()
        if (expression == ""):
            raise Exception("Empty expression provided.")
        return expression
