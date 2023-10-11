from models.image_node import ImageNode


class ImageSlide:
    """
    순환 이중 연결 리스트 클래스
    """

    def __init__(self):
        self.__head: 'ImageNode' = None
        self.__current: 'ImageNode' = None

    def is_empty(self) -> bool:
        """
        리스트가 비어있는지 확인하는 함수
        """
        return self.__head is None

    def append(self, new_node: 'ImageNode'):
        """
        맨 뒤(Tail)에 노드를 추가하고 현재 노드를 추가한 노드로 설정하는 함수
        """
        if self.is_empty():
            self.__head = new_node
            new_node.set_prev(new_node)
            new_node.set_next(new_node)
        else:
            tail = self.__head.get_prev()
            tail.set_next(new_node)
            new_node.set_prev(tail)
            new_node.set_next(self.__head)
            self.__head.set_prev(new_node)

        self.__current = new_node

    def delete_current(self):
        """
        current_node를 삭제하는 함수
        """

        # 리스트가 비어있거나 현재 노드가 None이면 함수를 종료한다.
        if self.is_empty() or self.__current is None:
            return

        print(f"delete current node: {self.__current.get_image_name()}")

        # 리스트에 노드가 하나만 있으면 리스트를 초기화한다.
        if self.__head.get_next() == self.__head:
            self.__head = None
            self.__current = None
            return

        # 삭제할려는 노드가 head 노드인 경우
        if self.__current == self.__head:
            tail = self.__head.get_prev()
            self.__head = self.__head.get_next()
            self.__head.set_prev(tail)
            tail.set_next(self.__head)
            self.__current = self.__head
        # 삭제할려는 노드가 일반 노드인 경우
        else:
            prev_node = self.__current.get_prev()
            next_node = self.__current.get_next()
            prev_node.set_next(next_node)
            next_node.set_prev(prev_node)
            self.__current = next_node

    def display(self):
        """
        리스트를 출력하는 함수
        """
        if self.is_empty():
            return
        current = self.__head
        s = "* <-> "
        while True:
            if current == self.__current:
                s += f"✅ {current.get_image_name()}  <-> "
            else:
                s += f"   {current.get_image_name()}  <-> "
            current = current.get_next()
            if current == self.__head:
                break
        s += "*"
        print(s)

    def merge(self, other: 'ImageSlide'):
        """
        다른 리스트와 현재 리스트를 병합하는 함수
        """
        if other.is_empty():
            return

        if self.is_empty():
            self.__head = other.__head
        else:
            self_head_prev = self.__head.get_prev()
            other_head_prev = other.__head.get_prev()
            self_head_prev.set_next(other.__head)
            other_head_prev.set_next(self.__head)
            self.__head.set_prev(other_head_prev)
            other.__head.set_prev(self_head_prev)

        # other 리스트를 초기화한다.
        other.__head = None

        # current 노드를 설정한다.
        self.__current = self.__head

    def get_current(self):
        if self.__current is None:
            return None
        else:
            return self.__current.get_image_path()

    def next_image(self):
        """
        다음 슬라이드를 반환하는 함수
        """
        if self.is_empty():
            return None
        else:
            self.__current = self.__current.get_next()
            return self.__current.get_image_path()

    def prev_image(self):
        """
        이전 슬라이드를 반환하는 함수
        """
        if self.is_empty():
            return None
        else:
            self.__current = self.__current.get_prev()
            return self.__current.get_image_path()
