class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class Queue:
    def __init__(self, node: "Node" = None):
        self.size = 0
        if node is not None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.head = None
            self.tail = None

    def enqueue(self, node: "Node"):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self) -> "Node":
        if self.head is not None:
            return_value = self.head
            self.head = self.head.next
            self.size -= 1
        else:
            raise Exception("Queue is empty")
        return return_value

    def rotate(self):
        """
        큐의 맨 앞에 있는 데이터를 맨 뒤로 이동시킵니다.
        """
        if self.size <= 1:
            return  # 큐의 크기가 1 이하일 때는 아무 작업도 수행하지 않습니다

        front_node = self.head
        self.head = front_node.next
        front_node.next = None  # 앞 요소를 떼어내고 끝을 None으로 설정

        self.tail.next = front_node  # 앞 요소를 현재 맨 뒤의 다음으로 설정
        self.tail = front_node  # 맨 뒷 요소를 업데이트

    def __repr__(self) -> str:
        cur_node = self.head
        out_list = []
        while cur_node is not None:
            out_list.append(str(cur_node.data))
            cur_node = cur_node.next

        return "-->".join(out_list)


if __name__ == "__main__":

    # Queue 클래스를 사용하여 큐를 생성합니다.
    my_queue = Queue()

    # enqueue 메서드를 사용하여 데이터를 큐에 추가합니다.
    my_queue.enqueue(Node(1))
    my_queue.enqueue(Node(2))
    my_queue.enqueue(Node(3))

    # 큐의 크기를 얻어옵니다.
    queue_size = my_queue.size
    print(f"큐의 크기: {queue_size}")  # 출력: 큐의 크기: 3

    # 큐 내부를 출력합니다.
    print(my_queue)  # 출력: 1-->2-->3

    # 큐의 맨 앞에 있는 데이터를 확인합니다.
    front_element = my_queue.head
    print(f"큐의 맨 앞 데이터: {front_element.data}")  # 출력: 큐의 맨 앞 데이터: 1

    # dequeue 메서드를 사용하여 큐에서 요소를 제거합니다.
    dequeued_node = my_queue.dequeue()
    print(f"제거된 요소: {dequeued_node.data}")  # 출력: 제거된 요소: 1

    # 큐의 크기를 다시 확인합니다.
    queue_size = my_queue.size
    print(f"큐의 크기: {queue_size}")  # 출력: 큐의 크기: 2

    # 큐 내부를 출력합니다.
    print(my_queue)  # 출력: 2-->3

    # rotate 메서드를 사용하여 큐의 맨 앞 데이터를 맨 뒤로 이동시킵니다.
    my_queue.rotate()

    # 큐를 다시 출력합니다.
    print(my_queue)  # 출력: 3-->2
