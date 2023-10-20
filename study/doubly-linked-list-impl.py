from typing import Any


class Node:
    def __init__(self, data: Any, prev: 'Node' = None, next: 'Node' = None) -> None:
        self._data = data
        self._prev = prev
        self._next = next

    @property
    def data(self):
        return self._data

    @property
    def prev(self):
        return self._prev

    @property
    def next(self):
        return self._next

    @data.setter
    def data(self, data: Any):
        self._data = data

    @prev.setter
    def prev(self, node: 'Node'):
        self._prev = node

    @next.setter
    def next(self, node: 'Node'):
        self._next = node

    def __str__(self) -> str:
        return f"Node({self.data})"

    def __repr__(self) -> str:
        return f"Node({self.data})"


class DoublyLinkedList:
    def __init__(self, first_node: 'Node' = None) -> None:
        self._head = first_node
        self._tail = first_node
        self._size = self._count()

    def _count(self) -> int:
        count = 0
        cur_node = self._head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        cur_node = self._head
        if self._size == 0:
            return None

        return_str = ""
        while cur_node is not None:
            return_str += f"{cur_node.data} <-> "
            cur_node = cur_node.next
        return_str += f"End of Doubly Linked List"
        return return_str

    def __iter__(self):
        return _DoublyLinkedListIterator(self._head)

    def head(self) -> 'Node':
        return self._head

    def append(self, new_node: "Node") -> bool:
        try:
            if self._size == 0:
                self._head = new_node
                self._tail = new_node
            else:
                self._tail.next = new_node
                new_node.prev = self._tail
                self._tail = new_node
            self._size += 1
            return True
        except Exception as e:
            print(e)
            return False

    def insert(self, new_node: "Node", index_number: int) -> bool:
        index_counter = 0
        cur_node = self._head

        # index_number가 0일 경우 맨 앞에 노드를 삽입합니다.
        if index_number == 0:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
            self._size += 1
            return True

        # 이전 노드와 다음 노드를 저장하면서 index_number에 도달합니다.
        while cur_node is not None:
            if index_number == index_counter:
                pred_node = cur_node.prev  # 이전 노드의 next를 현재 노드로 변경
                pred_node.next = new_node
                new_node.prev = pred_node
                new_node.next = cur_node
                cur_node.prev = new_node
                self._size += 1
                return True
            else:
                pred_node = cur_node  # 이전 노드를 저장
                cur_node = cur_node.next  # 다음 노드로 이동
                index_counter += 1
        return False

    def remove(self, target_value: int) -> bool:
        cur_node = self._head

        while cur_node is not None:
            if cur_node.data == target_value:
                pred_node = cur_node.prev
                if pred_node:
                    pred_node.next = cur_node.next
                if cur_node.next:
                    cur_node.next.prev = pred_node
                del cur_node
                self._size -= 1
                return True
            else:
                cur_node = cur_node.next
        return False


class _DoublyLinkedListIterator:
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


if __name__ == "__main__":
    # DoublyLinkedList 클래스를 사용하여 이중 연결 리스트를 생성합니다.
    my_doubly_linked_list = DoublyLinkedList(Node(1))

    # append 메서드를 사용하여 새로운 노드를 리스트에 추가합니다.
    my_doubly_linked_list.append(Node(2))
    my_doubly_linked_list.append(Node(3))

    # 이중 연결 리스트 내부를 출력합니다.
    # 출력: 1 <-> 2 <-> 3 <-> End of Doubly Linked List
    print(my_doubly_linked_list)

    # insert 메서드를 사용하여 노드를 특정 위치에 삽입합니다.
    new_node = Node(4)
    inserted = my_doubly_linked_list.insert(new_node, 1)  # 인덱스 1에 노드를 삽입
    if inserted:
        print("노드를 삽입했습니다.")
    else:
        print("삽입 실패")

    # 이중 연결 리스트 내부를 다시 출력합니다.
    # 출력: 1 <-> 4 <-> 2 <-> 3 <-> End of Doubly Linked List
    print(my_doubly_linked_list)

    # remove 메서드를 사용하여 특정 값을 가진 노드를 삭제합니다.
    removed = my_doubly_linked_list.remove(2)  # 값 2를 가진 노드 삭제
    if removed:
        print("노드를 삭제했습니다.")
    else:
        print("삭제 실패")

    # 이중 연결 리스트 내부를 다시 출력합니다.
    # 출력: 1 <-> 4 <-> 3 <-> End of Doubly Linked List
    print(my_doubly_linked_list)

    # 이중 연결 리스트를 순회하여 출력합니다.
    for node in my_doubly_linked_list:
        print(node)  # 출력: Node(1), Node(4), Node(3)
