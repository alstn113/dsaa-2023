class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @data.setter
    def data(self, data):
        self._data = data

    @next.setter
    def next(self, node):
        self._next = node

    def __str__(self):
        return f"Node({self.data})"

    def __repr__(self):
        return f"Node({self.data})"
