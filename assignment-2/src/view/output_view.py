class OutputView:
    def __init__(self):
        pass

    def print(self, message):
        print(message)

    def printError(self, message):
        self.print(message)

    def printHistory(self, history):
        for line in history:
            print(line)
