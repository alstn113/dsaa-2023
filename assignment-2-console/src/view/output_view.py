class OutputView:
    def __init__(self):
        pass

    def print(self, message):
        print(message)

    def print_error(self, message):
        self.print(message)

    def print_history(self, history):
        for line in history:
            print(line)
