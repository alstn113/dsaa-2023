from domain.Node import Node
from typing import Any


class Stack:
    """
    top이 head인 stack
    """

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, data: Any):
        if self._top is None:
            self._top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self._top
            self._top = new_node
        self._size += 1

    def pop(self) -> "Node":
        if self.is_empty():
            raise Exception("Stack is empty")

        popped = self._top
        self._top = self._top.next
        self._size -= 1
        return popped

    def peek(self) -> "Node":
        return self._top

    def __repr__(self):
        if self._top is None:
            return "stack 상태 : EMPTY"
        else:
            temp = self._top
            output_list = []
            while temp is not None:
                output_list.append(temp.data)
                temp = temp.next
            output_list.reverse()
            return f"stack 상태 : {' -> '.join(output_list)}"

    def is_empty(self) -> bool:
        return self._size == 0
