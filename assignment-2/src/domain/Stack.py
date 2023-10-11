from domain.Node import Node

# top이 head인 stack


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        else:
            popped = self.top.data
            self.top = self.top.next
            self.size -= 1
            return popped

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data

    def display(self):
        if self.top is None:
            return "stack 상태 : EMPTY"
        else:
            temp = self.top
            s = []
            while temp is not None:
                s.append(temp.data)
                temp = temp.next
            s.reverse()
            return f"stack 상태 : {' -> '.join(s)}"

    def is_empty(self):
        return self.size == 0
