from typing import Any


class Node:
    def __init__(self, data: Any, next: 'Node' = None) -> None:
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @data.setter
    def data(self, data: Any):
        self._data = data

    @next.setter
    def next(self, node: 'Node'):
        self._next = node

    def __str__(self) -> str:
        return f"Node({self.data})"

    def __repr__(self) -> str:
        return f"Node({self.data})"

    def __add__(self, other: 'Node') -> None:
        self.next = other


class LinkedList:
    def __init__(self, first_node: 'Node' = None) -> None:
        self._head = first_node
        self._tail = first_node
        if first_node is not None:
            self._size = 1
        else:
            self._size = self._count()

    def __contains__(self, data: Any) -> bool:
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == data:
                return True
            cur_node = cur_node.next
        return False

    def _count(self) -> int:
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        cur_node = self.head
        if self._size == 0:
            return None

        return_str = ""
        while cur_node is not None:
            return_str += f"{cur_node.data} -> "
            cur_node = cur_node.next
        return_str += f"End of Linked List"
        return return_str

    def __iter__(self):
        return _BagIterator(self._head)

    @property
    def head(self) -> 'Node':
        return self._head

    def append(self, new_node: "Node") -> bool:
        try:
            if self._size == 0:
                self._head = new_node
                self._tail = new_node
            else:
                self._tail.next = new_node
                self._tail = new_node
            self._size += 1
            return True
        except Exception as e:
            print(e)
            return False

    def insert(self, new_node: "Node", index_number: int) -> bool:
        index_counter = 0
        cur_node = self.head

        if index_number == 0:
            new_node.next = self._head
            self._head = new_node
            self._size += 1
            return True

        while cur_node is not None:
            if index_number == index_counter:
                pred_node.next = new_node
                new_node.next = cur_node
                self._size += 1
                return True
            else:
                pred_node = cur_node
                cur_node = cur_node.next
                index_counter += 1
        return False

    def remove(self, target_value: int) -> bool:
        cur_node = self.head

        while cur_node is not None:
            if cur_node.data == target_value:
                pred_node.next = cur_node.next
                del (cur_node)
                self._size -= 1
                return True
            else:
                pred_node = cur_node
                cur_node = cur_node.next
        return False


class _BagIterator():
    def __init__(self, head_node: "Node") -> 'Node':
        self._cur_node = head_node

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            return node
